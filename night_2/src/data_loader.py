import json
import psycopg2
import logging

from datetime import date

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
    Load data from a CSV file into the PostgreSQL database table.\n
    Args:
        file_path (str): Path to the JSON file containing the database credentials.
    Returns:
        credentials (dict): A dictionary containing database connection credentials.
    """
    # Read the database credentials from a JSON file.
    with open(file_path, 'r') as file:
        credentials = json.load(file)
    logging.info("Read credentials from JSON file.")
    return credentials


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


def load_data(conn, file_path) -> None:
    """
    Load data from a CSV file into the PostgreSQL database table.\n
    Args:
        conn (psycopg2.connect): A connection object to the PostgreSQL database.
        file_path (str): Path to the CSV file containing the data to load.
    """
    # Open a cursor to perform database operations.
    cursor = conn.cursor()
    with open(file_path, 'r', encoding='utf-8') as file:
        # Skip the header row if present in the CSV file.
        next(file)
        # Use the COPY command to load data into the specified table.
        cursor.copy_expert(f"""
            COPY bronze_layer.raw_data(person_name, personal_number, birth_date, address, phone_number, email,
                        ip_address, card_provider, card_number, iban, cvv, card_expire, currency_code, transaction_currency,
                        transacted_at, transaction_amount, transaction_number, from_country, to_country, record_id)
            FROM STDIN
            WITH CSV HEADER DELIMITER ',' QUOTE '"'
        """, file)
    # Commit the data loading operation to the database.   
    conn.commit()
    # Close the cursor and connection to free resources.
    cursor.close()
    conn.close()
    logging.info("Data loaded into database successfully.")


if __name__ == "__main__":
    # Initialize the process.
    print(softserve)

    # Define variables.
    data_file = f"night_1/data/data_{date.today()}.csv"
    credentials_path = "night_1/src/credentials.json"

    # Read credentials.
    all_credentials = read_credentials(credentials_path)
    bdn_credentials = all_credentials["bdn_db"]

    # Connect to BDN database.
    bdn_conn = connect_db(bdn_credentials)

    # Load data to database.
    load_data(bdn_conn, data_file)
    