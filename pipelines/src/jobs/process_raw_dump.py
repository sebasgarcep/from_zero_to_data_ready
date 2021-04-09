def process_raw_dump(context):
    context.environment.create_blank_directory(context.bucket_names.mdb_bucket)
    context.environment.create_blank_directory(context.bucket_names.csv_bucket)
    context.cloud.download_file(context.bucket_names.mdb_bucket, "database.mdb")
    context.mdbtools.dump_tables("{}/{}".format(context.bucket_names.mdb_bucket, "database.mdb"), context.bucket_names.csv_bucket)
    context.cloud.upload_bucket(context.bucket_names.csv_bucket)