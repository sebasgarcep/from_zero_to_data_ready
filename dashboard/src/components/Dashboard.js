import React from 'react';
import Grid from '@material-ui/core/Grid';
import ChartRenderer from './ChartRenderer';
import DashboardItem from './DashboardItem';
import { graphs } from '../constants';

const CustomDashboardItem = ({ item }) => (
    <Grid item xs={12} lg={6} key={item.id}>
        <DashboardItem title={item.name}>
            <ChartRenderer vizState={item.vizState} />
        </DashboardItem>
    </Grid>
);

const DashboardPage = () => (
    <Grid
        container
        spacing={3}
        style={{ padding: 24 }}
        justify="space-around"
        alignItems="flex-start"
    >
        {graphs.map(item => <CustomDashboardItem item={item} />)}
    </Grid>
);

export default DashboardPage;
