from collections import OrderedDict

class Runner:
    def __init__(self):
        self.context = None
        self.jobs = OrderedDict()

    def set_context(self, context):
        self.context = context

    def register_job(self, name, job):
        self.jobs[name] = job

    def run_jobs(self):
        names = self.context.environment.get_jobs()
        for item in names:
            job = self.jobs[item]
            job(self.context)