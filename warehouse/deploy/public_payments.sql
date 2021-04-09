-- Deploy warehouse:public_payments to pg

BEGIN;

CREATE TABLE public.payments (
    invoice_id int NOT NULL,
    invoice_date date NULL,
    type text NULL,
    amount int NULL
);

COMMIT;
