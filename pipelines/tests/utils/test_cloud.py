import unittest
from unittest.mock import call, patch, Mock
import os
from src.utils.cloud import Cloud

@patch("src.utils.cloud.storage")
class TestCloud(unittest.TestCase):
    def test_init(self, mock_storage):
        """
        should correctly initialize the storage client
        """
        cloud = Cloud()
        mock_storage.Client.from_service_account_json.assert_called_with("service_account.json")

    def test_download_blob(self, mock_storage):
        """
        should download a blob from cloud storage
        """
        cloud = Cloud()
        blob = Mock()
        blob.name = "filename"
        cloud.download_blob("bucket", blob)
        blob.download_to_filename.assert_called_with(os.path.realpath("./data/bucket/filename"))

    def test_download_file(self, mock_storage):
        """
        should download from cloud storage using file name
        """
        storage = Mock()
        bucket = Mock()
        blob = Mock()
        blob.name = "filename"
        mock_storage.Client.from_service_account_json.return_value = storage
        storage.bucket.return_value = bucket
        bucket.blob.return_value = blob

        cloud = Cloud()
        cloud.download_file("bucket", "filename")
        
        storage.bucket.assert_called_with("bucket")
        bucket.blob.assert_called_with("filename")
        blob.download_to_filename.assert_called_with(os.path.realpath("./data/bucket/filename"))

    def test_download_bucket(self, mock_storage):
        """
        should download all files in a bucket from cloud storage
        """
        storage = Mock()
        first_blob = Mock()
        first_blob.name = "first_filename"
        second_blob = Mock()
        second_blob.name = "second_filename"
        mock_storage.Client.from_service_account_json.return_value = storage
        storage.list_blobs.return_value = [first_blob, second_blob]

        cloud = Cloud()
        cloud.download_bucket("bucket")

        storage.list_blobs.assert_called_with("bucket")
        first_blob.download_to_filename.assert_called_with(os.path.realpath("./data/bucket/first_filename"))
        second_blob.download_to_filename.assert_called_with(os.path.realpath("./data/bucket/second_filename"))

    def test_upload_file(self, mock_storage):
        """
        should upload file to cloud storage
        """
        storage = Mock()
        bucket = Mock()
        blob = Mock()
        storage.bucket.return_value = bucket
        bucket.blob.return_value = blob
        mock_storage.Client.from_service_account_json.return_value = storage

        cloud = Cloud()
        cloud.upload_file("bucket", "filename")

        storage.bucket.assert_called_with("bucket")
        bucket.blob.assert_called_with("filename")
        blob.upload_from_filename.assert_called_with(os.path.realpath("./data/bucket/filename"))

    @patch("src.utils.cloud.os.listdir", lambda *args: ["first_filename", "second_filename"])
    def test_upload_bucket(self, mock_storage):
        """
        should upload data folder to cloud storage bucket
        """
        storage = Mock()
        bucket = Mock()
        first_blob = Mock()
        first_blob.name = "first_filename"
        second_blob = Mock()
        second_blob.name = "second_filename"
        storage.bucket.return_value = bucket
        bucket.blob.side_effect = lambda blob_name: first_blob if blob_name == "first_filename" else second_blob
        mock_storage.Client.from_service_account_json.return_value = storage

        cloud = Cloud()
        cloud.upload_bucket("bucket")

        storage.bucket.assert_called_with("bucket")
        bucket.blob.assert_has_calls([call("first_filename"), call("second_filename")])
        first_blob.upload_from_filename.assert_called_with(os.path.realpath("./data/bucket/first_filename"))
        second_blob.upload_from_filename.assert_called_with(os.path.realpath("./data/bucket/second_filename"))