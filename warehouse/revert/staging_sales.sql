-- Revert warehouse:staging_sales from pg

BEGIN;

DROP TABLE staging.sales;

COMMIT;
