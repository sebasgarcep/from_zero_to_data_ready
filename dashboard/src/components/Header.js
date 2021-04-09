import React from 'react';
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';
import MenuItem from '@material-ui/core/MenuItem';
import MultiSelect from './MultiSelect';
import { clothingTypes, silhouettes } from '../constants';
import { useFilterContext } from '../utils';

const useStyles = makeStyles((theme) => ({
    container: {
      display: 'flex',
      flexWrap: 'wrap',
    },
    textField: {
      marginLeft: theme.spacing(1),
      marginRight: theme.spacing(1),
      width: 200,
    },
    chips: {
        display: 'flex',
        flexWrap: 'wrap',
    },
    chip: {
        margin: 2,
    },
}));

const Header = () => {
    const classes = useStyles();
    const { filterContext, setFilterValue } = useFilterContext();

    return (
        <form className={classes.container}>
            <TextField
                label="Initial Date"
                type="date"
                value={filterContext.initialDate}
                onChange={evt => setFilterValue('initialDate', evt.target.value)}
                className={classes.textField}
                InputLabelProps={{ shrink: true }}
            />
            <TextField
                label="Final Date"
                type="date"
                value={filterContext.finalDate}
                className={classes.textField}
                InputLabelProps={{ shrink: true }}
            />
            <MultiSelect
                id="clothing-type"
                label="Clothing Type"
                value={filterContext.clothingTypes}
                onChange={evt => setFilterValue('clothingTypes', evt.target.value)}
            >
                {clothingTypes.map(it => <MenuItem key={it} value={it}>{it}</MenuItem>)}
            </MultiSelect>
            <MultiSelect
                id="silhouette"
                label="Silhouette"
                value={filterContext.silhouettes}
                onChange={evt => setFilterValue('silhouettes', evt.target.value)}
            >
                {silhouettes.map(it => <MenuItem key={it} value={it}>{it}</MenuItem>)}
            </MultiSelect>
        </form>
    );
};

export default Header;
