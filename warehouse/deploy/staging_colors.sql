-- Deploy warehouse:staging_colors to pg

BEGIN;

CREATE TABLE staging.colors (
    id int PRIMARY KEY,
    description text NULL
);

COMMIT;
