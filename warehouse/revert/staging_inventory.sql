-- Revert warehouse:staging_inventory from pg

BEGIN;

DROP TABLE staging.inventory;

COMMIT;
