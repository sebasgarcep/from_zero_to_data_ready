import json
from sqlalchemy import create_engine

class Warehouse:
    def __init__(self):
        with open("warehouse_account.json", "r") as file_handle:
            credentials = json.load(file_handle)
        host = credentials["host"]
        port = credentials["port"]
        dbname = credentials["dbname"]
        user = credentials["user"]
        password = credentials["password"]
        self.connection_string = "postgresql://%s:%s@%s:%s/%s" % (user, password, host, port, dbname)
        self.connection = create_engine(self.connection_string)

    def upload_dataframe(self, schema_name, table_name, df):
        self.connection.execute("TRUNCATE TABLE %s.%s" % (schema_name, table_name))
        df.to_sql(table_name, self.connection, schema_name, if_exists = "append", index = False)

    def execute_sql(self, statement):
        return self.connection.execute(statement)