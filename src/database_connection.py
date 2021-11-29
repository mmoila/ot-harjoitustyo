import os
import sqlite3
from config import DATABASE_FILENAME

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(DATABASE_FILENAME)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
