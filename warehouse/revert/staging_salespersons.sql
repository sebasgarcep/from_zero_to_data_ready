-- Revert warehouse:staging_salespersons from pg

BEGIN;

DROP TABLE staging.salespersons;

COMMIT;
