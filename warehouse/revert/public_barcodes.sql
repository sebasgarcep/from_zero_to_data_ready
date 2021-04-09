-- Revert warehouse:public_barcodes from pg

BEGIN;

DROP TABLE public.barcodes;

COMMIT;
