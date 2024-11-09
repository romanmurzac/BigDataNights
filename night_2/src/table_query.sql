CREATE TABLE IF NOT EXISTS bronze_layer.raw_data (
    person_name VARCHAR(50)
    ,personal_number BIGINT
    ,birth_date DATE
    ,address VARCHAR(250)
    ,phone_number VARCHAR(25)
    ,email VARCHAR(50)
    ,ip_address VARCHAR(20)
    ,card_provider VARCHAR(50)
    ,card_number BIGINT
    ,iban VARCHAR(25)
    ,cvv INT
    ,card_expire VARCHAR(10)
    ,currency_code VARCHAR(10)
    ,transaction_currency VARCHAR(50)
    ,transacted_at TIMESTAMP
    ,transaction_amount INT
    ,transaction_number VARCHAR(50)
    ,from_country VARCHAR(50)
    ,to_country VARCHAR(50)
    ,record_id VARCHAR(50)
);
