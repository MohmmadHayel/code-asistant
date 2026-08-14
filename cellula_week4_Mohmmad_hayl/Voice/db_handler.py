import sqlite3
import pandas as pd


class DBHandler:
    def __init__(self, db_path=":memory:"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)

    def load_csv(self, csv_path: str, table_name: str = "data_table") -> list[str]:
        df = pd.read_csv(csv_path)
        df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]
        df.to_sql(table_name, self.conn, if_exists="replace", index=False)
        return list(df.columns)

    def execute_query(self, query: str) -> list[dict]:
        cursor = self.conn.cursor()
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        rows = cursor.fetchall()
        return [dict(zip(columns, row)) for row in rows]