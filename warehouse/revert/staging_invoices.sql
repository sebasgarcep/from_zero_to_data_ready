-- Revert warehouse:staging_invoices from pg

BEGIN;

DROP TABLE staging.invoices;

COMMIT;
