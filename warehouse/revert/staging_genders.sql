-- Revert warehouse:staging_genders from pg

BEGIN;

DROP TABLE staging.genders;

COMMIT;
