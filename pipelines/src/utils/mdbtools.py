import os
import subprocess
from src.utils.data import get_data_path

class MdbTools:
    def get_tables(self, filename):
        file_path = get_data_path(filename)
        result = subprocess.check_output(["mdb-tables", "-1", file_path])
        return [item.strip().decode() for item in result.splitlines() if item.strip().decode() != ""]

    def export_table(self, dbname, tablename, folder_path):
        db_path = get_data_path(dbname)
        filename = os.path.join(folder_path, "%s.csv" % tablename.replace("/", " "))
        file_path = get_data_path(filename)
        command = ["mdb-export", db_path, tablename]
        result = subprocess.check_output(command)
        with open(file_path, "wb") as file_handle:
            file_handle.write(result)
        return filename

    def dump_tables(self, filename, folder_path):
        tables = []
        for tablename in self.get_tables(filename):
            item = self.export_table(filename, tablename, folder_path)
            tables.append(item)
        return tables
