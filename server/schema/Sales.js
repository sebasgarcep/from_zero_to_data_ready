cube('Sales', {
    sql: `
        SELECT
            invoice_id
            ,invoice_date
            ,barcode
            ,discount_percentage
            ,price
        FROM sales
    `,

    joins: {
        Barcodes: {
            relationship: 'belongsTo',
            sql: `${Sales}.barcode = ${Barcodes}.barcode`,
        },

        Invoices: {
            relationship: 'belongsTo',
            sql: `${Sales}.invoice_id = ${Invoices}.id AND ${Sales}.invoice_date = ${Invoices}.date`,
        },
    },

    measures: {
        total_revenue: {
            type: 'sum',
            sql: 'price * (1 - discount_percentage)',
            format: 'currency',
        },
    },

    dimensions: {
        surrogate_key: {
            type: 'string',
            sql: `${Payments}.invoice_id || '-' || ${Payments}.invoice_date || '-' || ${Payments}.barcode`,
            primaryKey: true,
        },
    
        discount_percentage: {
            type: 'number',
            sql: 'discount_percentage',
            format: 'percent',
        },

        price: {
            type: 'number',
            sql: 'price',
            format: 'currency',
        },
    },
});