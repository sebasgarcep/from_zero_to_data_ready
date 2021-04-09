import unittest
from unittest.mock import Mock, PropertyMock
from src.jobs.process_raw_dump import process_raw_dump

class TestProcessRawDump(unittest.TestCase):
    def test_process(self):
        """
        should correctly process the mdb dump in cloud storage and upload the exported csvs
        """
        context_calls = []
        context = Mock()

        context.bucket_names.mdb_bucket = "mdb_bucket"
        context.bucket_names.csv_bucket = "csv_bucket"

        context.environment.create_blank_directory.side_effect = \
            lambda dirname: context_calls.append(("environment.create_blank_directory", dirname))
        context.cloud.download_file.side_effect = \
            lambda bucket, filename: context_calls.append(("cloud.download_file", bucket, filename))
        context.mdbtools.dump_tables.side_effect = \
            lambda filename, folder_path: context_calls.append(("mdbtools.dump_tables", filename, folder_path))
        context.cloud.upload_bucket.side_effect = \
            lambda bucket: context_calls.append(("cloud.upload_bucket", bucket))

        process_raw_dump(context)

        expected_calls = [
            ("environment.create_blank_directory", "mdb_bucket"),
            ("environment.create_blank_directory", "csv_bucket"),
            ("cloud.download_file", "mdb_bucket", "database.mdb"),
            ("mdbtools.dump_tables", "mdb_bucket/database.mdb", "csv_bucket"),
            ("cloud.upload_bucket", "csv_bucket")
        ]

        self.assertListEqual(context_calls, expected_calls)