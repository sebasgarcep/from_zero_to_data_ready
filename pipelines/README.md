# Pipelines

This project is in charge of all data load and transformations (ETLs) required to make everything work. All data pipelines will run on Python. Even though Python is not the most efficient language, it allows us to leverage exploratory data analysis without requiring rewriting much of the code. The data pipelines are:

## process_raw_dump
Downloads the `.mdb` file from `mdb_bucket`, dumps all tables into `.csv` files and uploads them to the `csv_bucket` bucket.

## process_csv_dump
Downloads certain `.csv` files from `csv_bucket`, process and cleans the data, and finally uploads the dataframes into the `staging` schema of the database.

## populate_warehouse
Once the raw data is loaded into staging tables in the data warehouse, this pipeline is in charge of populating production tables with the data, and making any necessary transformations to it.

## How to setup

To setup this project you need to copy the `service_account.json`, `warehouse_account.json`, and `bucket_names.json` files into this directory. You also need to have either Python and Pipenv installed, or have Docker.

## How to run

Then you can run it with:

```bash
$ docker build -t pipelines .
$ docker run -e "JOBS=job1,job2" pipelines
```

If instead you wish to run pipelines without docker then use the following commands:

```bash
$ pipenv shell
$ pipenv install
$ JOBS=job1,job2 python3 ./main.py
```

## How to test

To run tests we need to execute the following commands:

```bash
$ docker build -t test_pipelines --build-arg PYTHON_ENV=testing -f Testing.Dockerfile .
$ docker run test_pipelines
```