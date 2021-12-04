from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()
    tables = ["cash_flow", "users", "budgets"]

    for table in tables:
        sql = "DROP TABLE IF EXISTS " + table + ";"
        cursor.execute(sql)
        connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.executescript("""
        CREATE TABLE budgets (
            id INTEGER PRIMARY KEY,
            name TEXT,
            user_id INTEGER REFERENCES users
        );
        
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        );

        CREATE TABLE cash_flow (
            id INTEGER PRIMARY KEY,
            description TEXT,
            count INTEGER,
            is_income INTEGER,
            budget_id INTEGER REFERENCES budgets ON DELETE CASCADE
        )

    """)
    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
