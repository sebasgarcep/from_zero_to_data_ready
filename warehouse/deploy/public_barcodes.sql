-- Deploy warehouse:public_barcodes to pg

BEGIN;

CREATE TABLE public.barcodes (
	barcode text PRIMARY KEY,
	reference text NULL,
	clothing_type_id int NULL,
    clothing_type_description text NULL,
	gender_id int NULL,
    gender_description text NULL,
	silhouette_id int NULL,
    silhouette_description text NULL,
	color_id int NULL,
    color_description text NULL,
	size_id text NULL,
	size_description text NULL,
    quantity int NOT NULL,
    damaged int NOT NULL
);

COMMIT;
