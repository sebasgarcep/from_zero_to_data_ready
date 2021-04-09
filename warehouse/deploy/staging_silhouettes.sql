-- Deploy warehouse:staging_silhouettes to pg

BEGIN;

CREATE TABLE staging.silhouettes (
    id int PRIMARY KEY,
    description text NULL
);

COMMIT;
