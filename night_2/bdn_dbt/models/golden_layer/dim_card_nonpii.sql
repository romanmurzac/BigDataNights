{{ config(
    schema='golden_layer',
    materialized='table'
) }}

WITH staging_data AS (
    SELECT
        card_provider,
        CONCAT('***', RIGHT(CAST(card_number AS TEXT), 4)) AS masked_card_number,
        iban,
        '***' AS masked_cvv,
        CONCAT('**/**') AS masked_card_expire,
        currency_code,
        transaction_currency
    FROM
        {{ ref('dim_card') }}
)

SELECT
    *
FROM
    staging_data