-- Deploy warehouse:public_sales to pg

BEGIN;

CREATE TABLE public.sales (
    invoice_id int NOT NULL,
    invoice_date date NULL,
    barcode text NULL,
    discount_percentage double precision NULL,
    price int NULL
);

COMMIT;
