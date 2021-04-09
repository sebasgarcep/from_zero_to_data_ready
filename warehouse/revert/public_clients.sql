-- Revert warehouse:public_clients from pg

BEGIN;

DROP TABLE public.clients;

COMMIT;
