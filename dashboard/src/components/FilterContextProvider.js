import React, { useState } from 'react';
import { filterContextInitialState, FilterContext } from '../utils';

const FilterContextProvider = ({ children }) => {
    const [filterContext, setFilterContext] = useState(filterContextInitialState);

    return (
        <FilterContext.Provider value={[filterContext, setFilterContext]}>
            {children}
        </FilterContext.Provider>
    );
};

export default FilterContextProvider;