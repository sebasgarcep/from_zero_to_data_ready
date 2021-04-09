import os
from google.cloud import storage
from src.utils.data import get_data_path

class Cloud:
    def __init__(self):
        self.storage = storage.Client.from_service_account_json("service_account.json")

    def download_blob(self, bucket, file_blob):
        file_path = get_data_path(bucket, file_blob.name)
        file_blob.download_to_filename(file_path)

    def download_file(self, bucket, filename):
        file_bucket = self.storage.bucket(bucket)
        file_blob = file_bucket.blob(filename)
        self.download_blob(bucket, file_blob)

    def download_bucket(self, bucket):
        for file_blob in self.storage.list_blobs(bucket):
            self.download_blob(bucket, file_blob)

    def upload_file(self, bucket, filename):
        file_bucket = self.storage.bucket(bucket)
        file_blob = file_bucket.blob(filename)
        file_path = get_data_path(bucket, filename)
        file_blob.upload_from_filename(file_path)

    def upload_bucket(self, bucket):
        for filename in os.listdir(get_data_path(bucket)):
            self.upload_file(bucket, filename)

