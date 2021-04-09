-- Deploy warehouse:staging_sizes to pg

BEGIN;

CREATE TABLE staging.sizes (
    id text PRIMARY KEY
);

COMMIT;
