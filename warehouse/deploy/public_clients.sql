-- Deploy warehouse:public_clients to pg

BEGIN;

CREATE TABLE public.clients (
    id numeric(30) PRIMARY KEY,
    name text NULL,
    address text NULL,
    city text NULL,
    email text NULL,
    work_phone text NULL,
    cellphone text NULL,
    neighborhood text NULL,
    birthday date NULL,
    home_phone text NULL
);

COMMIT;
