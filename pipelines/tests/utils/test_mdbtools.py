import unittest
from unittest.mock import patch, Mock
import os
from src.utils.data import get_data_path
from src.utils.mdbtools import MdbTools
from src.utils.environment import Environment

class TestMdbTools(unittest.TestCase):
    mdbtools = None

    def setUp(self):
        self.mdbtools = MdbTools()

    @patch(
        "src.utils.mdbtools.get_data_path",
        lambda *paths: os.path.realpath("./mocks/test_store/test_database.mdb")
    )
    def test_get_tables(self):
        """
        should return names of all tables inside an .mdb file
        """
        result = self.mdbtools.get_tables("test_store/test_database.mdb")
        self.assertListEqual(result, ["Part", "Product"])

    @patch(
        "src.utils.mdbtools.get_data_path",
        lambda *paths: os.path.realpath("./mocks/test_store/test_database.mdb") \
            if paths[0] == "test_store/test_database.mdb" \
            else get_data_path(*paths)
    )
    def test_export_table(self):
        """
        should export table into a csv file
        """
        environment = Environment()
        environment.create_blank_directory("test_store")
        self.mdbtools.export_table("test_store/test_database.mdb", "Part", "test_store")
        with open("./data/test_store/Part.csv", "r", encoding = "UTF-8") as contents_handle:
            with open("./mocks/test_store/Part.csv", "r", encoding = "UTF-8") as comparison_handle:
                contents = contents_handle.read()
                comparison = comparison_handle.read()
                self.assertEqual(contents, comparison)

    @patch(
        "src.utils.mdbtools.get_data_path",
        lambda *paths: os.path.realpath("./mocks/test_store/test_database.mdb") \
            if paths[0] == "test_store/test_database.mdb" \
            else get_data_path(*paths)
    )
    def test_dump_tables(self):
        """
        should export all tables in the database into csv files
        """
        environment = Environment()
        environment.create_blank_directory("test_store")
        self.mdbtools.dump_tables("test_store/test_database.mdb", "test_store")
        file_list = ["Part", "Product"]
        for filename in file_list:
            with open("./data/test_store/%s.csv" % filename, "r", encoding = "UTF-8") as contents_handle:
                with open("./mocks/test_store/%s.csv" % filename, "r", encoding = "UTF-8") as comparison_handle:
                    contents = contents_handle.read()
                    comparison = comparison_handle.read()
                    self.assertEqual(contents, comparison)