import json
import psycopg2
import logging

from psycopg2 import sql

from softserve import softserve

# Configure logging.
logging.basicConfig(
    level=logging.INFO,                    
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)


def read_credentials(file_path: str) -> dict:
    """
    Read database credentials from a JSON file.\n
    Args:
        file_path (str): Path to the JSON file containing the database credentials.
    Returns:
        credentials (dict): A dictionary containing database connection credentials.
    """
    # Read the database credentials from the specified JSON file.
    with open(file_path, 'r') as file:
        credentials = json.load(file)
    logging.info("Read credentials from JSON file.")
    return credentials


def read_sql(file_path: str) -> str:
    """
    Read SQL queries from a file.\n
    Args:
        file_path (str): Path to the SQL file containing the queries.
    Returns:
        sql_query (str): The SQL query as a string.
    """
    # Read the SQL file to retrieve the query.
    with open(file_path, 'r') as sql_file:
        sql_query = sql_file.read()
    logging.info("Read SQL query from sql file.")
    return sql_query


def connect_db(credentials: dict) -> psycopg2.connect:
    """
    Establish a connection to the PostgreSQL database.\n
    Args:
        credentials (dict): A dictionary containing database connection credentials.
    Returns:
        conn (psycopg2.connect): A connection object to the PostgreSQL database.
    """
    # Connect to the PostgreSQL server using the provided credentials.
    conn = psycopg2.connect(
        dbname=credentials['dbname'],
        user=credentials['user'],
        password=credentials['password'],
        host=credentials['host'],
        port=credentials['port']
    )
    logging.info("Create database connection.")
    return conn


def create_db(conn: psycopg2.connect, db_name: str) -> None:
    """
    Create a new database in PostgreSQL.\n
    Args:
        conn (psycopg2.connect): A connection object to the PostgreSQL server.
        db_name (str): The name of the database to be created.
    """
    # Set autocommit to True to allow CREATE DATABASE command outside of a transaction block.
    conn.autocommit = True
    # Open a cursor to perform database operations.
    cur = conn.cursor()
    # SQL to create a database.
    create_db_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name))
    # Execute the query.
    cur.execute(create_db_query)
    # Close the connection and cursor.
    cur.close()
    conn.close()
    logging.info("Create database.")


def create_object(conn: psycopg2.connect, creation_query: str) -> None:
    """
    Execute a SQL command to create a database object, a table or schema.\n
    Args:
        conn (psycopg2.connect): A connection object to the PostgreSQL database.
        creation_query (str): The SQL query to create the database object.
    """
    # Open a cursor to perform database operations.
    cur = conn.cursor()
    # Execute the provided SQL command for creation.
    cur.execute(creation_query)
    # Commit the changes to the database.
    conn.commit()
    # Close the cursor and connection to free resources.
    cur.close()
    conn.close()
    logging.info("Create table / schema.")


if __name__ == "__main__":
    # Initialize the process.
    print(softserve)

    # Define variables.
    bdn_db = "bdn_db"
    credentials_path = "night_1/src/credentials.json"
    schema_sql = "night_1/src/schema_query.sql"
    table_sql = "night_1/src/table_query.sql"

    # Read credentials.
    all_credentials = read_credentials(credentials_path)
    default_credentials = all_credentials["default_db"]
    bdn_credentials = all_credentials["bdn_db"]

    # Connect to default database.
    default_conn = connect_db(default_credentials)

    # Create BDN database.
    create_db(default_conn, bdn_db)

    # Connect to BDN database.
    bdn_conn = connect_db(bdn_credentials)

    # Read schema query.
    schema_query = read_sql(schema_sql)

    # Read table query.
    table_query = read_sql(table_sql)

    # Create bronze schema.
    create_object(bdn_conn, schema_query)

    # Connect to BDN database.
    bdn_conn = connect_db(bdn_credentials)

    # Create raw data table.
    create_object(bdn_conn, table_query)
