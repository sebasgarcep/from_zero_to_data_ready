import unittest
from unittest.mock import patch, Mock
import builtins
from src.utils.warehouse import Warehouse

@patch("src.utils.warehouse.json.load", lambda *args: {
    "host": "host",
    "port": "port",
    "dbname": "dbname",
    "user": "user",
    "password": "password",
})
@patch.object(builtins, "open")
@patch("src.utils.warehouse.create_engine")
class TestWarehouse(unittest.TestCase):
    def test_init(self, mock_create_engine, mock_open):
        """
        should correctly initialize the connection to the data warehouse
        """
        warehouse = Warehouse()
        self.assertEqual(warehouse.connection_string, "postgresql://user:password@host:port/dbname")
        mock_create_engine.assert_called_with("postgresql://user:password@host:port/dbname")
        self.assertIsNotNone(warehouse.connection)

    def test_upload_dataframe(self, mock_create_engine, mock_open):
        """
        should clear out table and upload dataframe to data warehouse
        """
        engine = Mock()
        mock_create_engine.return_value = engine
        df = Mock()
        warehouse = Warehouse()
        warehouse.upload_dataframe("schema", "table", df)
        engine.execute.assert_called_with("TRUNCATE TABLE schema.table")
        df.to_sql.assert_called_with("table", engine, "schema", if_exists = "append", index = False)

    def test_execute_sql(self, mock_create_engine, mock_open):
        """
        should execute arbitrary sql statement and return results
        """
        engine = Mock()
        engine.execute.return_value = "MOCK_RESULT"
        mock_create_engine.return_value = engine
        warehouse = Warehouse()
        result = warehouse.execute_sql("SELECT * FROM table")
        engine.execute.assert_called_with("SELECT * FROM table")
        self.assertEqual(result, "MOCK_RESULT")