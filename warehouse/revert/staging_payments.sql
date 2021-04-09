-- Revert warehouse:staging_payments from pg

BEGIN;

DROP TABLE staging.payments;

COMMIT;
