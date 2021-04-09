-- Deploy warehouse:StagingSchema to pg

BEGIN;

CREATE SCHEMA staging;

COMMIT;
