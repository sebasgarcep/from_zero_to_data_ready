-- Deploy warehouse:staging_inventory to pg

BEGIN;

CREATE TABLE staging.inventory (
    barcode text PRIMARY KEY,
    quantity int NOT NULL,
    damaged int NOT NULL
);

COMMIT;
