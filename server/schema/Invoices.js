cube('Invoices', {
    sql: `
        SELECT
            id
            ,date
            ,salesperson_id
            ,salesperson_description
            ,(date + time) AS time
            ,client_id
        FROM invoices
    `,

    joins: {
        Clients: {
            relationship: 'belongsTo',
            sql: `${Invoices}.client_id = ${Clients}.id`,
        },

        Payments: {
            relationship: 'hasMany',
            sql: `${Invoices}.id = ${Payments}.invoice_id AND ${Invoices}.date = ${Payments}.invoice_date`,
        },

        Sales: {
            relationship: 'hasMany',
            sql: `${Invoices}.id = ${Sales}.invoice_id AND ${Invoices}.date = ${Sales}.invoice_date`,
        },
    },

    measures: {
        count: {
            type: 'count',
        },
    },

    dimensions: {
        surrogate_key: {
            type: 'string',
            sql: `${Invoices}.id || '-' || ${Invoices}.date`,
            primaryKey: true,
        },

        id: {
            type: 'number',
            sql: 'id',
        },

        salesperson_id: {
            type: 'number',
            sql: 'salesperson_id',
        },

        salesperson_description: {
            type: 'number',
            sql: 'salesperson_description',
        },

        time: {
            type: 'time',
            sql: 'time',
        },
    },
});