import random
import csv
import logging

from faker import Faker
from datetime import date

from softserve import softserve

# Configure logging.
logging.basicConfig(
    level=logging.INFO,                    
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)


def create_data(locale: str) -> Faker:
    """
    Creates a Faker instance for generating localized synthetic data.
    Args:
        locale (str): The locale code for the desired synthetic data language/region.
    Returns:
        Faker: An instance of the Faker class configured with the specified locale.
    """
    # Log the action.
    logging.info(f"Created synthetic data for {locale.split('_')[-1]} country code.")
    return Faker(locale)


def generate_record(synthetic: Faker) -> list:
    """
    Generates a single synthetic user record.
    Args:
        synthetic (Faker): A Faker instance for generating random data.
    Returns:
        list: A list containing various synthetic user details such as name, username, email, etc.
    """
    # Generate personal data.
    person_name = synthetic.name() # Generate person name.
    personal_number = synthetic.ssn()  # Generate a social security number.
    birth_date = synthetic.date_of_birth(None, 18, 70)  # Generate a birth date.
    address = synthetic.address().replace("\n", ", ")  # Replace newlines in the address with commas.

    # Generate contact data.
    phone_number = synthetic.phone_number()  # Generate a phone number.
    email = person_name.replace(" ", "").lower()+"@"+synthetic.free_email_domain() # Generate email with a random email domain.
    ip_address = synthetic.ipv4()  # Generate a IPv4 address.

    # Generate credit card data.
    card_provider = synthetic.credit_card_provider() # Generate card provider.
    card_number = synthetic.credit_card_number() # Generate credit card number.
    iban = synthetic.iban()  # Generate an IBAN.
    cvv = synthetic.credit_card_security_code() # Generate CVV.
    card_expire = synthetic.credit_card_expire() # Generate expiration date.

    # Generate transaction data.
    currency = synthetic.currency() # Generate pair of code and currency.
    currency_code = currency[0] # Generate currency code.
    transaction_currency = currency[1] # Generate currency.
    transacted_at = synthetic.date_time_between("-1d", "now")  # Generate a date within the last day.
    transaction_amount = random.randint(0, 1_000_000)  # Generate transaction amount up to 1 million.
    transaction_number = synthetic.uuid4() # Generate transaction number.
    from_country = synthetic.country() # Generate country from where was made the transaction.
    to_country = synthetic.country() # Generate country to where was made the transaction.

    # Add record id.
    record_id = synthetic.uuid4() # Generate unique record id.

    # Return all the generated data as a list.
    return [
        person_name, personal_number, birth_date,
        address, phone_number, email, ip_address, card_provider,
        card_number, iban, cvv, card_expire, currency_code,
        transaction_currency, transacted_at, transaction_amount,
        transaction_number, from_country, to_country, record_id
    ]


def write_to_csv(file_path: str) -> None:
    """
    Generates multiple synthetic user records and writes them to a CSV file.
    Args:
        file_path (str): The path where the CSV file will be saved.
    """
    # Create a Faker instance with Romanian data.
    synthetic = create_data("ro_RO")
    
    # Define the CSV headers.
    headers = [
        "person_name", "personal_number", "birth_date",
        "address", "phone_number", "email", "ip_address", "card_provider",
        "card_number", "iban", "cvv", "card_expire", "currency_code",
        "transaction_currency", "transacted_at", "transaction_amount",
        "transaction_number", "from_country", "to_country", "record_id"
    ]

    # Open the CSV file for writing.
    with open(file_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
        # Generate and write each record to the CSV.
        no_records = random.randint(101_101, 303_303)
        for _ in range(no_records):
            writer.writerow(generate_record(synthetic))
    # Log the action.
    logging.info(f"Written {no_records} records to the CSV file.")


if __name__ == "__main__":
    # Initialize the process.
    print(softserve)

    # Logging starting of the process.
    logging.info(f"Starting data generation for {date.today()}...")

    # Define the output file name with today's date.
    output_file = f"night_1/data/data_{date.today()}.csv"

    # Generate and write records to the CSV.
    write_to_csv(output_file)

    # Logging ending of the process.
    logging.info(f"Finished data generation for {date.today()}.")
    