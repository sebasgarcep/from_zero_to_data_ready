-- Revert warehouse:StagingSchema from pg

BEGIN;

DROP SCHEMA staging;

COMMIT;
