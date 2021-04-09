-- Revert warehouse:public_payments from pg

BEGIN;

DROP TABLE public.payments;

COMMIT;
