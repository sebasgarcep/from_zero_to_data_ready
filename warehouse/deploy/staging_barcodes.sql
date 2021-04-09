-- Deploy warehouse:StagingBarcodes to pg

BEGIN;

CREATE TABLE staging.barcodes (
	barcode text PRIMARY KEY,
	reference text NULL,
	clothing_type_id int NULL,
	gender_id int NULL,
	silhouette_id int NULL,
	color_id int NULL,
	size_id text NULL
);

COMMIT;
