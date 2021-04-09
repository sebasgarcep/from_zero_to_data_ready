import unittest
from unittest.mock import patch
from src.utils.runner import Runner
from src.start import get_runner, start

class TestStart(unittest.TestCase):
    def test_all_jobs_registered(self):
        """
        all jobs should be registered on the runner
        """
        runner = get_runner()
        job_list = runner.jobs.keys()
        self.assertIn("process_raw_dump", job_list)
        self.assertIn("process_csv_dump", job_list)
        self.assertIn("populate_warehouse", job_list)

    @patch.object(Runner, "run_jobs")
    @patch.object(Runner, "set_context")
    @patch("src.start.Context")
    def test_starts_correctly(self, mock_Context, mock_set_context, mock_run_jobs):
        """
        should initialize runner context and run jobs on start
        """
        run_order = []
        
        def set_context_side_effect(*args):
            self.assertNotEqual(len(args), 0)
            self.assertIsNotNone(args[0])
            run_order.append(1)
        mock_set_context.side_effect = set_context_side_effect

        def run_jobs_side_effect(*args):
            run_order.append(2)
        mock_run_jobs.side_effect = run_jobs_side_effect

        start()

        self.assertListEqual(run_order, [1, 2])