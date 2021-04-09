-- Deploy warehouse:staging_salespersons to pg

BEGIN;

CREATE TABLE staging.salespersons (
    id text PRIMARY KEY
);

COMMIT;
