import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

<<<<<<< HEAD
DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)
=======
DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
>>>>>>> 763bdcb0d4f8648d87af9c0fff0ff19ba2ce273f
