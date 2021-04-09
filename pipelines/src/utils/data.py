import os

def get_data_path(*paths):
    return os.path.realpath(os.path.join("./data", *paths))