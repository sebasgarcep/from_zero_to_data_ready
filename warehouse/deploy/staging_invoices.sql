-- Deploy warehouse:staging_invoices to pg

BEGIN;

CREATE TABLE staging.invoices (
    id int NOT NULL,
    date date NULL,
    salesperson_id text NULL,
    client_id numeric(30) NULL,
    time time NULL,
    PRIMARY KEY(id, date)
);

COMMIT;
