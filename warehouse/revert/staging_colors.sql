-- Revert warehouse:staging_colors from pg

BEGIN;

DROP TABLE staging.colors;

COMMIT;
