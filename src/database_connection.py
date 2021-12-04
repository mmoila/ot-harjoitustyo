import sqlite3
from config import DATABASE_FILE_PATH

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row
connection.cursor().execute("PRAGMA foreign_keys = ON")


def get_database_connection():
    return connection
