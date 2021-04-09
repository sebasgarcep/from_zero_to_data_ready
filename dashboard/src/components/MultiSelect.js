import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Select from '@material-ui/core/Select';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';
import Chip from '@material-ui/core/Chip';

const useStyles = makeStyles((theme) => ({
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

const MultiSelect = ({ id, label, value, onChange, children }) => {
    const classes = useStyles();
    return (
        <FormControl className={classes.textField}>
            <InputLabel id={`${id}-label`}>{label}</InputLabel>
            <Select
                id={id}
                labelId={`${id}-label`}
                multiple
                value={value}
                onChange={onChange}
                renderValue={(selected) => (
                    <div className={classes.chips}>
                        {selected.map((value) => (
                            <Chip key={value} label={value} className={classes.chip} />
                        ))}
                    </div>
                )}
            >
                {children}
            </Select>
        </FormControl>
    );
};

export default MultiSelect;