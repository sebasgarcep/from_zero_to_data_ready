# Server
This server exposes the data from the PostgreSQL database (and any other data sources that may be used in the future), so that clients have a single source of truth for their data analytic workloads.

## How to setup
The server runs on NodeJS and requires Yarn for package management. Once in the root directory of the server, run the following command to install libraries:

```bash
$ yarn install
```

Additionally, you must either add an `.env` file to the root directory of the server, or add the following env variables to the deployment environment:

```
CUBEJS_DB_HOST=<Host address of the database>
CUBEJS_DB_NAME=<Name of the database>
CUBEJS_DB_USER=<User of the database>
CUBEJS_DB_PASS=<Password of the database>
CUBEJS_WEB_SOCKETS=true
CUBEJS_DB_TYPE=postgres
CUBEJS_API_SECRET=<Some long, random string to be used internally by the application>
CUBEJS_EXTERNAL_DEFAULT=true
```

These variables are documented [here](https://cube.dev/docs/reference/environment-variables).

## How to run
Once dependencies are installed, you can start the application using:

```bash
$ yarn start:prod
```

If you are performing dev work, then you should run the app in development mode:

```bash
$ yarn start:dev
```