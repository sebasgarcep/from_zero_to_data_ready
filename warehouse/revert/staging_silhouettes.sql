-- Revert warehouse:staging_silhouettes from pg

BEGIN;

DROP TABLE staging.silhouettes;

COMMIT;
