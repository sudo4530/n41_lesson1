import os
from dotenv import load_dotenv
import psycopg2 as db
load_dotenv()


class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database=os.getenv("Database"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            host=os.getenv("LOCALHOST"),
        )
        cursor = database.cursor()
        cursor.execute(query)
        data = ["insert", "create", "delete", "update"]
        if query_type in data:
            database.commit()
            if query_type == "insert":
                return "Inserted"