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
            budget_id INTEGER REFERENCES budgets
        )

    """)
    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)
   

def insert_test_budgets(connection):
    cursor = connection.cursor()
    cursor.executescript("""
        INSERT INTO budgets (name, user_id) values ("test", 1);
        INSERT INTO budgets (name, user_id) values ("test2", 2);
        INSERT INTO budgets (name, user_id) values ("test3", 3);
        INSERT INTO budgets (name, user_id) values ("test4", 4);

    """)
    connection.commit()

def insert_test_cash_flow(connection):
    cursor = connection.cursor()
    cursor.executescript("""
        INSERT INTO cash_flow (count, is_income, budget_id) values (200, 1, 1);
        INSERT INTO cash_flow (count, is_income, budget_id) values (300, 1, 2);
        INSERT INTO cash_flow (count, is_income, budget_id) values (400, 1, 3);
        INSERT INTO cash_flow (count, is_income, budget_id) values (500, 0, 4);

    """)
    connection.commit()


if __name__ == "__main__":
    initialize_database()
   