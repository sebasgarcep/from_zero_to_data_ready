cube('Payments', {
    sql: `
        SELECT
            invoice_id
            ,invoice_date
            ,type
            ,amount
        FROM payments
    `,

    joins: {
        Invoices: {
            relationship: 'belongsTo',
            sql: `${Payments}.invoice_id = ${Invoices}.id AND ${Payments}.invoice_date = ${Invoices}.date`,
        },
    },

    measures: {
        total_amount: {
            type: 'sum',
            sql: 'amount',
        },
    },

    dimensions: {
        surrogate_key: {
            type: 'string',
            sql: `${Payments}.invoice_id || '-' || ${Payments}.invoice_date || '-' || ${Payments}.type`,
            primaryKey: true,
        },

        type: {
            type: 'string',
            sql: 'type',
        },

        amount: {
            type: 'number',
            sql: 'amount',
        },
    },
});