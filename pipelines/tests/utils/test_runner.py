import unittest
from unittest.mock import Mock
from src.utils.runner import Runner

class TestRunner(unittest.TestCase):
    runner = None

    def setUp(self):
        self.runner = Runner()

    def test_set_context(self):
        """
        should correctly set the context for the runner
        """
        context = {}
        self.runner.set_context(context)
        self.assertEqual(self.runner.context, context)

    def test_register_job(self):
        """
        should correctly set a job
        """
        job = lambda *args: None
        self.runner.register_job("test_job", job)
        self.assertIn("test_job", self.runner.jobs)
        self.assertEqual(self.runner.jobs["test_job"], job)

    def test_run_jobs(self):
        """
        should run all jobs that were registered to it in the order they were registered
        """
        run_order = []

        first_job = lambda *args: run_order.append(1)
        second_job = lambda *args: run_order.append(2)
        third_job = lambda *args: run_order.append(3)

        self.runner.register_job("first_job", first_job)
        self.runner.register_job("second_job", second_job)
        self.runner.register_job("third_job", third_job)

        context = Mock()
        environment = Mock()
        environment.get_jobs = lambda *args: ["first_job", "second_job", "third_job"]
        context.environment = environment
        self.runner.set_context(context)

        self.runner.run_jobs()

        self.assertListEqual(run_order, [1, 2, 3])
        