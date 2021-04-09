import os
from shutil import rmtree
from src.utils.data import get_data_path

class Environment:
    def get_jobs(self):
        job_list = os.environ.get("JOBS")
        if job_list is None:
            return []
        return [item.strip() for item in job_list.split(",") if item.strip() != ""]

    def create_blank_directory(self, dirname):
        dirpath = get_data_path(dirname)
        if os.path.exists(dirpath):
            rmtree(dirpath)
        os.mkdir(dirpath)