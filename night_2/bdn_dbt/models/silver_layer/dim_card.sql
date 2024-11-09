{{ config(
    schema='silver_layer',
    materialized='table'
) }}

SELECT
    card_number,
    card_provider,
    iban,
    cvv,
    card_expire,
    currency_code,
    transaction_currency
FROM
    {{ source('bronze_layer', 'raw_data') }}
