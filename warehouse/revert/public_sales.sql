-- Revert warehouse:public_sales from pg

BEGIN;

DROP TABLE public.sales;

COMMIT;
