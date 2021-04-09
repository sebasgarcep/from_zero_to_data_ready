# Warehouse
Our data warehouse will be a postgres database as the data is not big enough to merit using Redshift or similar products. To manage migrations we will be using a tool called `sqitch`.

## Schemas

In order to have better control of our data, the data warehouse is partitioned into the following schemas:
### staging
This schema holds data uploaded by the data pipelines into the data warehouse.

### public
This schema holds public-facing tables.

## Development
To create a migration using `sqitch` we run the command:

```bash
$ sqitch add <migration_name> -n "<description>"
```

This creates three files: `deploy/<migration_name>` which should hold the migration logic, `revert/<migration_name>` which should hold the logic for reverting our changes, and `verify/<migration_name>` which should hold logic meant to validate that the schema changes were applied succesfully. In our case we will not be implementing verification scripts.

## Deployment
To deploy our migrations to the target database we run the following command:

```bash
$ sqitch deploy --target db:pg://<user>:<password>@<host>:<port>/<dbname>
```

