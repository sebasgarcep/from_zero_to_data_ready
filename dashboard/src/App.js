import './body.css';
import React from 'react';
import cubejs from '@cubejs-client/core';
import { makeStyles } from '@material-ui/core/styles';
import { CubeProvider } from '@cubejs-client/react';
import Header from './components/Header';
import Dashboard from './components/Dashboard';
import FilterContextProvider from './components/FilterContextProvider';

const API_URL = process.env.REACT_APP_SERVER_HOST;
const CUBEJS_TOKEN = process.env.REACT_APP_SERVER_TOKEN;

const cubejsApi = cubejs(CUBEJS_TOKEN, {
    apiUrl: `${API_URL}/cubejs-api/v1`,
});

const useStyles = makeStyles(() => ({
    root: {
        flexGrow: 1,
    },
}));

const App = () => {
    const classes = useStyles();
    return (
        <CubeProvider cubejsApi={cubejsApi}>
            <FilterContextProvider>
                <div className={classes.root}>
                    <Header />
                    <Dashboard />
                </div>
            </FilterContextProvider>
        </CubeProvider>
    );
};

export default App;
