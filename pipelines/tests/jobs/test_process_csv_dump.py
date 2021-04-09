import unittest
from unittest.mock import patch, Mock, PropertyMock
import os
import shutil
from src.utils.environment import Environment
from src.jobs.process_csv_dump import process_csv_dump

@patch(
    "src.jobs.process_csv_dump.get_data_path",
    lambda *paths: os.path.realpath(os.path.join("./mocks", *paths))
)
class TestProcessCsvDump(unittest.TestCase):
    def test_context_calls(self):
        """
        should correctly call context functions
        """
        context_calls = []
        context = Mock()

        context.bucket_names.mdb_bucket = "mdb_bucket"
        context.bucket_names.csv_bucket = "csv_bucket"

        def environment_create_blank_directory_side_effect(dirname):
            context_calls.append(("environment.create_blank_directory", dirname))
        context.environment.create_blank_directory.side_effect = environment_create_blank_directory_side_effect
        
        def cloud_download_file_side_effect(bucket, filename):
            context_calls.append(("cloud.download_file", bucket, filename))
        context.cloud.download_file.side_effect = cloud_download_file_side_effect
        
        def warehouse_upload_dataframe_side_effect(schema, table, df):
            context_calls.append(("warehouse.upload_dataframe", schema, table))
        context.warehouse.upload_dataframe.side_effect = warehouse_upload_dataframe_side_effect

        process_csv_dump(context)

        expected_calls = [
            ("environment.create_blank_directory", "csv_bucket"),
            ("cloud.download_file", "csv_bucket", "T-Codigos de barras.csv"),
            ("cloud.download_file", "csv_bucket", "T-Lista colores.csv"),
            ("cloud.download_file", "csv_bucket", "T-Tipo de prenda.csv"),
            ("cloud.download_file", "csv_bucket", "T-Sexo.csv"),
            ("cloud.download_file", "csv_bucket", "T-Lista siluetas.csv"),
            ("cloud.download_file", "csv_bucket", "T-Lista tallas.csv"),
            ("cloud.download_file", "csv_bucket", "T-Datos cliente.csv"),
            ("cloud.download_file", "csv_bucket", "T-Factura.csv"),
            ("cloud.download_file", "csv_bucket", "T-FacturaOriginal.csv"),
            ("cloud.download_file", "csv_bucket", "T-Factura cotizacion.csv"),
            ("cloud.download_file", "csv_bucket", "T-Factura cotizacion2.csv"),
            ("cloud.download_file", "csv_bucket", "T-Vendedoras.csv"),
            ("cloud.download_file", "csv_bucket", "T-Inventario.csv"),
            ("cloud.download_file", "csv_bucket", "T-Inventario dañado.csv"),
            ("cloud.download_file", "csv_bucket", "T-Ventas.csv"),
            ("cloud.download_file", "csv_bucket", "T-Ventas1.csv"),
            ("cloud.download_file", "csv_bucket", "T-Cotizaciones.csv"),
            ("cloud.download_file", "csv_bucket", "T-CotizacionesOriginal.csv"),
            ("cloud.download_file", "csv_bucket", "T-Formas de pago.csv"),
            ("cloud.download_file", "csv_bucket", "T-Formas de pago Cotizaciones.csv"),
            ("warehouse.upload_dataframe", "staging", "barcodes"),
            ("warehouse.upload_dataframe", "staging", "colors"),
            ("warehouse.upload_dataframe", "staging", "clothing_types"),
            ("warehouse.upload_dataframe", "staging", "genders"),
            ("warehouse.upload_dataframe", "staging", "silhouettes"),
            ("warehouse.upload_dataframe", "staging", "sizes"),
            ("warehouse.upload_dataframe", "staging", "inventory"),
            ("warehouse.upload_dataframe", "staging", "clients"),
            ("warehouse.upload_dataframe", "staging", "salespersons"),
            ("warehouse.upload_dataframe", "staging", "invoices"),
            ("warehouse.upload_dataframe", "staging", "sales"),
            ("warehouse.upload_dataframe", "staging", "payments"),
        ]

        self.assertListEqual(context_calls, expected_calls)

    def test_process(self):
        """
        should correctly process the csv data in cloud storage and insert it into the data warehouse
        """
        environment = Environment()
        environment.create_blank_directory("staging_tables_store")

        context = Mock()

        context.bucket_names.mdb_bucket = "mdb_bucket"
        context.bucket_names.csv_bucket = "csv_bucket"

        context.warehouse.upload_dataframe.side_effect = \
            lambda _, table, df: df.to_csv(os.path.join("./data/staging_tables_store", "%s.csv" % table), index = False)

        process_csv_dump(context)

        tables = [
            "barcodes",
            "colors",
            "clothing_types",
            "genders",
            "silhouettes",
            "sizes",
            "inventory",
            "clients",
            "salespersons",
            "invoices",
            "sales",
            "payments",
        ]

        for item in tables:
            with open(os.path.join("./data/staging_tables_store", "%s.csv" % item), "r") as contents_handle:
                with open(os.path.join("./mocks/staging_tables_store", "%s.csv" % item), "r") as comparison_handle:
                    contents = contents_handle.read()
                    comparison = comparison_handle.read()
                    self.assertEqual(contents, comparison)