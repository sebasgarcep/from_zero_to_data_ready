import { createContext, useContext } from 'react';

export const filterContextInitialState = {
    initialDate: '2018-01-01',
    finalDate: '2019-12-31',
    clothingTypes: [],
    silhouettes: [],
};

export const FilterContext = createContext([filterContextInitialState, () => {}]);

export const useFilterContext = () => {
    const [filterContext, setFilterContext] = useContext(FilterContext);

    const setFilterValue = (filterName, filterValue) => {
        setFilterContext({ ...filterContext, [filterName]: filterValue })
    };

    const getTimeDimensions = (timeDimensions = []) => {
        if (!filterContext.initialDate || !filterContext.finalDate) {
            return timeDimensions;
        }
        return timeDimensions.map(item => {
            if (item.dimension === "Invoices.time") {
                return {
                    ...item,
                    dateRange: [filterContext.initialDate, filterContext.finalDate],
                };
            } else {
                return item;
            }
        });
    };

    const getFilters = (filters = []) => {
        filters = [...filters];

        if (filterContext.clothingTypes.length > 0) {
            filters.push({
                "member": "Barcodes.clothing_type_description",
                "operator": "equals",
                "values": filterContext.clothingTypes,
            });
        }

        if (filterContext.silhouettes.length > 0) {
            filters.push({
                "member": "Barcodes.silhouette_description",
                "operator": "equals",
                "values": filterContext.silhouettes,
            });
        }

        return filters;
    }

    return {
        filterContext,
        setFilterValue,
        getFilters,
        getTimeDimensions,
    };
};