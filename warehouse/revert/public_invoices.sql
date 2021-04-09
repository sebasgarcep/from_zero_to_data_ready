-- Revert warehouse:public_invoices from pg

BEGIN;

DROP TABLE public.invoices;

COMMIT;
