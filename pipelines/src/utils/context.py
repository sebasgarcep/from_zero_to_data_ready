from src.utils.bucket_names import BucketNames
from src.utils.cloud import Cloud
from src.utils.environment import Environment
from src.utils.mdbtools import MdbTools
from src.utils.warehouse import Warehouse

class Context:
    def __init__(self):
        self.bucket_names = BucketNames()
        self.cloud = Cloud()
        self.environment = Environment()
        self.mdbtools = MdbTools()
        self.warehouse = Warehouse()