-- Revert warehouse:staging_clients from pg

BEGIN;

DROP TABLE stage.clients;

COMMIT;
