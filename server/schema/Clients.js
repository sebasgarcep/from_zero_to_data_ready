cube('Clients', {
    sql: `
        SELECT
            id
            ,name
            ,address
            ,city
            ,email
            ,work_phone
            ,cellphone
            ,neighborhood
            ,birthday
            ,home_phone
        FROM clients
    `,

    joins: {
        Invoices: {
            relationship: 'hasMany',
            sql: `${Clients}.id = ${Invoices}.client_id`,
        },
    },

    measures: {
        count: {
            type: 'count',
        },
    },

    dimensions: {
        id: {
            type: 'number',
            sql: 'id',
            primaryKey: true,
            shown: true,
        },

        name: {
            type: 'string',
            sql: 'name',
        },

        address: {
            type: 'string',
            sql: 'address',
        },

        city: {
            type: 'string',
            sql: 'city',
        },

        email: {
            type: 'string',
            sql: 'email',
        },

        work_phone: {
            type: 'string',
            sql: 'work_phone',
        },

        cellphone: {
            type: 'string',
            sql: 'cellphone',
        },

        neighborhood: {
            type: 'string',
            sql: 'neighborhood',
        },

        birthday: {
            type: 'time',
            sql: 'birthday',
        },

        home_phone: {
            type: 'string',
            sql: 'home_phone',
        },
    },
});