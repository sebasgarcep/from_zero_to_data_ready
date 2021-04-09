-- Deploy warehouse:public_invoices to pg

BEGIN;

CREATE TABLE public.invoices (
    id int NOT NULL,
    date date NULL,
    salesperson_id text NULL,
    salesperson_description text NULL,
    client_id numeric(30) NULL,
    time time NULL,
    PRIMARY KEY(id, date)
);


COMMIT;
