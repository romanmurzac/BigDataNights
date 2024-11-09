{{ config(
    schema='golden_layer',
    materialized='table'
) }}

WITH staging_data AS (
    SELECT
        card_provider,
        card_number,
        iban,
        cvv,
        card_expire,
        currency_code,
        transaction_currency
    FROM
        {{ ref('dim_card') }}
)

SELECT
    *
FROM
    staging_data