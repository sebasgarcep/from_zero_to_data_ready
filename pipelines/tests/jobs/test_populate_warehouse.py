import unittest
from unittest.mock import Mock
from src.jobs.populate_warehouse import populate_warehouse

class TestProcessRawDump(unittest.TestCase):
    def test_populate(self):
        """
        should populate production tables using tables from staging
        """
        context = Mock()

        populate_warehouse(context)

        context.warehouse.execute_sql.has_been_called()