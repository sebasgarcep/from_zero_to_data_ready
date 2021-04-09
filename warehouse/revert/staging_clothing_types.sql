-- Revert warehouse:staging_clothing_types from pg

BEGIN;

DROP TABLE staging.clothing_types;

COMMIT;
