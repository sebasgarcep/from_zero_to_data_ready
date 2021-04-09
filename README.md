# Retail Data Science
This project is meant to emulate a complete analytics project, end-to-end, using real data from a legacy application. All parts f the project are implemented using Test Driven Development, whenever possible.

## Setup
You will need the following files at the root level of the repo:
- A `service_account.json` file at the root of the repo with all necessary permissions to access google services.
- A `warehouse_account.json` file containing the credentials for the data warehouse database and subscribing to the following structure:

```json
{
    "host": "",
    "port": "",
    "dbname": "",
    "user": "",
    "password": ""
}
```
- A `bucket_names.json` file containing the names of the `mdb_bucket` where the `database.mdb` file is located and the `csv_bucket` where the output of the `mdb-export` should be saved.
```json
{
    "mdb_bucket": "",
    "csv_bucket": "",
}
```

## Notebooks
The `notebooks/` folder holds any Jupyter notebooks used for exploratory data analysis. 

## Cloud Architecture
All elements of the cloud architecture are described in this [README](./architecture/README.md).

## Data Pipelines
The data pipelines are described in this [README](./pipelines/README.md). 

## Data Warehouse
The data warehouse is described in this [README](./warehouse/README.md).

## Analytics Dashboard
The analytics dashboard is described in this [README](./dashboard/README.md).

## Analytics Server
The analytics server is described in this [README](./server/README.md).