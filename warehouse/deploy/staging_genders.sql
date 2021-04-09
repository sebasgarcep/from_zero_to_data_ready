-- Deploy warehouse:staging_genders to pg

BEGIN;

CREATE TABLE staging.genders (
    id int PRIMARY KEY,
    description text NULL
);

COMMIT;
