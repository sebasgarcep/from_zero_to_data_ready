-- Deploy warehouse:staging_clothing_types to pg

BEGIN;

CREATE TABLE staging.clothing_types (
    id int PRIMARY KEY,
    description text NULL
);

COMMIT;
