import unittest
from unittest.mock import patch
import builtins
from src.utils.bucket_names import BucketNames

@patch("src.utils.bucket_names.json.load", lambda *args: {
    "mdb_bucket": "mdb_bucket",
    "csv_bucket": "csv_bucket",
})
@patch.object(builtins, "open")
class TestBucketNames(unittest.TestCase):
    def test_init(self, mock_open):
        """
        should correctly initialize the bucket names
        """
        bucket_names = BucketNames()
        self.assertEqual(bucket_names.mdb_bucket, "mdb_bucket")
        self.assertEqual(bucket_names.csv_bucket, "csv_bucket")