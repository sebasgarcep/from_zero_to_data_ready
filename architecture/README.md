# Architecture
All the architecture will be hosted on Google Cloud.

## Cloud Storage
The storage holds raw data files pending to be processed. Ideally, client-facing products should query from the data warehouse to obtain data.

The buckets in Cloud Storage that we will use are:

### mdb_bucket
The raw database dump (an `.mdb` file) is deposited into the `mdb_bucket` bucket on Cloud Storage.

### csv_bucket
The tables in the database dump are exported into `csv` and deposited into this bucket.

## SQL Database
The SQL database will act as a data warehouse that will serve our analytics to the CubeJS server. We require a Postgres instance, but nothing too powerful.