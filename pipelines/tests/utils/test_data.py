import unittest
import os
from src.utils.data import get_data_path

class TestData(unittest.TestCase):
    def test_correct_path(self):
        result = get_data_path("part1")
        self.assertEqual(result, os.path.realpath("./data/part1"))
        result = get_data_path("part1", "part2.txt")
        self.assertEqual(result, os.path.realpath("./data/part1/part2.txt"))