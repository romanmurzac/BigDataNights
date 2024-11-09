{{ config(
    schema='silver_layer',
    materialized='table'
) }}

SELECT
    transaction_number,
    transacted_at,
    transaction_amount,
    from_country,
    to_country,
    record_id,
    personal_number,
    card_number
FROM
    {{ source('bronze_layer', 'raw_data') }}
