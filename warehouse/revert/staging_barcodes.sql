-- Revert warehouse:StagingBarcodes from pg

BEGIN;

DROP TABLE staging.barcodes;

COMMIT;
