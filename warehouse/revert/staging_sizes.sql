-- Revert warehouse:staging_sizes from pg

BEGIN;

DROP TABLE staging.sizes;

COMMIT;
