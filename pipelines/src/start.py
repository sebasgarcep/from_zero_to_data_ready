from src.jobs.populate_warehouse import populate_warehouse
from src.jobs.process_csv_dump import process_csv_dump
from src.jobs.process_raw_dump import process_raw_dump
from src.utils.context import Context
from src.utils.runner import Runner

def get_runner():
    runner = Runner()
    runner.register_job("process_raw_dump", process_raw_dump)
    runner.register_job("process_csv_dump", process_csv_dump)
    runner.register_job("populate_warehouse", populate_warehouse)
    return runner

def start():
    runner = get_runner()
    context = Context()
    runner.set_context(context)
    runner.run_jobs()