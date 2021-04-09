import unittest
from unittest.mock import patch
import os
from src.utils.environment import Environment

class TestEnvironment(unittest.TestCase):
    environment = None

    def setUp(self):
        self.environment = Environment()

    @patch(
        "src.utils.environment.os.environ.get",
        lambda key: None
    )
    def test_get_jobs_undefined(self):
        """
        should return empty list if jobs env variable is None (undefined)
        """
        result = self.environment.get_jobs()
        self.assertEqual(result, [])

    @patch(
        "src.utils.environment.os.environ.get",
        lambda key: "job1,job2"
    )
    def test_get_jobs_defined(self):
        """
        should return list of jobs from comma-separated env variable
        """
        result = self.environment.get_jobs()
        self.assertEqual(result, ["job1", "job2"])

    def test_create_blank_directory(self):
        """
        should create an empty folder inside the data folder
        """
        self.environment.create_blank_directory("environment_store")
        self.assertTrue(os.path.exists("./data/environment_store"))
        self.assertListEqual(os.listdir("./data/environment_store"), [])

    def test_recreate_directory(self):
        """
        should delete an existing folder with the same name and create it again with no contents
        """
        self.environment.create_blank_directory("environment_store")
        os.mkdir("./data/environment_store/interior_folder")
        open("./data/environment_store/file1", "w").close()
        open("./data/environment_store/interior_folder/file2", "w").close()
        self.environment.create_blank_directory("environment_store")
        self.assertTrue(os.path.exists("./data/environment_store"))
        self.assertListEqual(os.listdir("./data/environment_store"), [])
