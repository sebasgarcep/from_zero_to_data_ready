def populate_warehouse(context):
    # barcodes
    context.warehouse.execute_sql(
        """
        BEGIN TRANSACTION;
            TRUNCATE TABLE public.barcodes;
            INSERT INTO public.barcodes (
                barcode,
                reference,
                clothing_type_id,
                clothing_type_description,
                gender_id,
                gender_description,
                silhouette_id,
                silhouette_description,
                color_id,
                color_description,
                size_id,
                size_description,
                quantity,
                damaged
            )
            SELECT
                bc.barcode,
                bc.reference,
                bc.clothing_type_id,
                ct.description AS clothing_type_description,
                bc.gender_id,
                ge.description AS gender_description,
                bc.silhouette_id,
                sh.description AS silhouette_description,
                bc.color_id,
                co.description AS color_description,
                bc.size_id,
                bc.size_id AS size_description,
                COALESCE(iv.quantity, 0) AS quantity,
                COALESCE(iv.damaged, 0) AS damaged
            FROM staging.barcodes bc
            LEFT JOIN staging.clothing_types ct
                ON ct.id = bc.clothing_type_id
            LEFT JOIN staging.genders ge
                ON ge.id = bc.gender_id
            LEFT JOIN staging.silhouettes sh
                ON sh.id = bc.silhouette_id
            LEFT JOIN staging.colors co
                ON co.id = bc.color_id
            LEFT JOIN staging.inventory iv
                ON iv.barcode = bc.barcode
            ;
        COMMIT TRANSACTION;
        """
    )

    # clients
    context.warehouse.execute_sql(
        """
        BEGIN TRANSACTION;
            TRUNCATE TABLE public.clients;
            INSERT INTO public.clients (
                id,
                name,
                address,
                city,
                email,
                work_phone,
                cellphone,
                neighborhood,
                birthday,
                home_phone
            )
            SELECT
                id,
                name,
                address,
                city,
                email,
                work_phone,
                cellphone,
                neighborhood,
                birthday,
                home_phone
            FROM staging.clients
            ;
        COMMIT TRANSACTION;
        """
    )

    # invoices
    context.warehouse.execute_sql(
        """
        BEGIN TRANSACTION;
            TRUNCATE TABLE public.invoices;
            INSERT INTO public.invoices (
                id,
                date,
                salesperson_id,
                salesperson_description,
                client_id,
                time
            )
            SELECT
                id,
                date,
                salesperson_id,
                salesperson_id AS salesperson_description,
                client_id,
                time
            FROM staging.invoices
            WHERE NOT (id = 15865 AND date = '2012-01-27')
            ;
        COMMIT TRANSACTION;
        """
    )

    # payments
    context.warehouse.execute_sql(
        """
        BEGIN TRANSACTION;
            TRUNCATE TABLE public.payments;
            INSERT INTO public.payments (
                invoice_id,
                invoice_date,
                type,
                amount
            )
            SELECT
                invoice_id,
                invoice_date,
                type,
                amount
            FROM staging.payments
            WHERE NOT (invoice_id = 15865 AND invoice_date = '2012-01-27')
            ;
        COMMIT TRANSACTION;
        """
    )

    # sales
    context.warehouse.execute_sql(
        """
        BEGIN TRANSACTION;
            TRUNCATE TABLE public.sales;
            INSERT INTO public.sales (
                invoice_id,
                invoice_date,
                barcode,
                discount_percentage,
                price
            )
            SELECT
                invoice_id,
                invoice_date,
                barcode,
                discount_percentage,
                price
            FROM staging.sales
            WHERE NOT (invoice_id = 15865 AND invoice_date = '2012-01-27')
            ;
        COMMIT TRANSACTION;
        """
    )