# Analytics Dashboard

This project implements a React Dashboard that connects to a running CubeJS instance and allows end-users to track specific business analytics.

## How to setup
Install development dependencies by running:

```bash
$ yarn install
```

Additionally, you must either add an `.env` file to the root directory of the app, or add the following env variables to the build environment:

```
SKIP_PREFLIGHT_CHECK=true
REACT_APP_SERVER_HOST=<Host for the CubeJS server>
REACT_APP_SERVER_TOKEN=<Auth token for the CubeJS server>
```

## How to run
If you are performing dev work, then you should run the app in development mode:

```bash
$ yarn start
```

To create a CDN-ready build of the application run the following command.

```bash
$ yarn build
```