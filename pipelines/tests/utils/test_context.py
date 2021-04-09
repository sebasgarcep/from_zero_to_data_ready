import unittest
from unittest.mock import patch, Mock
from src.utils.context import Context

class TestContext(unittest.TestCase):
    @patch("src.utils.context.BucketNames", Mock(return_value = 1))
    @patch("src.utils.context.Cloud", Mock(return_value = 2))
    @patch("src.utils.context.Environment", Mock(return_value = 3))
    @patch("src.utils.context.MdbTools", Mock(return_value = 4))
    @patch("src.utils.context.Warehouse", Mock(return_value = 5))
    def test_context_sets_components(self):
        """
        should set all the components of the context object during init
        """
        context = Context()
        self.assertEqual(context.bucket_names, 1)
        self.assertEqual(context.cloud, 2)
        self.assertEqual(context.environment, 3)
        self.assertEqual(context.mdbtools, 4)
        self.assertEqual(context.warehouse, 5)