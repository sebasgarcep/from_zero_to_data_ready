cube('Barcodes', {
    sql: `
        SELECT
            barcode
            ,reference
            ,clothing_type_id
            ,clothing_type_description
            ,gender_id
            ,gender_description
            ,silhouette_id
            ,silhouette_description
            ,color_id
            ,color_description
            ,size_id
            ,size_description
            ,quantity
            ,damaged
        FROM barcodes
    `,

    joins: {
        Sales: {
            relationship: 'hasMany',
            sql: `${Barcodes}.barcode = ${Sales}.barcode`,
        },
    },

    measures: {
        total_quantity: {
            type: 'sum',
            sql: 'quantity',
        },

        total_damaged: {
            type: 'sum',
            sql: 'damaged',
        },
    },

    dimensions: {
        barcode: {
            type: 'string',
            sql: 'barcode',
            primaryKey: true,
            shown: true,
        },

        reference: {
            type: 'string',
            sql: 'reference',
        },

        clothing_type_id: {
            type: 'number',
            sql: 'clothing_type_id',
        },

        clothing_type_description: {
            type: 'string',
            sql: 'clothing_type_description',
        },

        gender_id: {
            type: 'number',
            sql: 'gender_id',
        },

        gender_description: {
            type: 'string',
            sql: 'gender_description',
        },

        silhouette_id: {
            type: 'number',
            sql: 'silhouette_id',
        },

        silhouette_description: {
            type: 'string',
            sql: 'silhouette_description',
        },

        color_id: {
            type: 'number',
            sql: 'color_id',
        },

        color_description: {
            type: 'string',
            sql: 'color_description',
        },

        size_id: {
            type: 'number',
            sql: 'size_id',
        },

        size_description: {
            type: 'string',
            sql: 'size_description',
        },

        quantity: {
            type: 'number',
            sql: 'quantity',
        },

        amount: {
            type: 'number',
            sql: 'amount',
        },
    },
});
