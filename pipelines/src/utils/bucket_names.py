import json

class BucketNames:
    def __init__(self):
        with open("bucket_names.json", "r") as file_handle:
            bucket_names = json.load(file_handle)
        self.mdb_bucket = bucket_names["mdb_bucket"]
        self.csv_bucket = bucket_names["csv_bucket"]

    