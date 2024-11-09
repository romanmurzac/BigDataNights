{{ config(
    schema='golden_layer',
    materialized='view'
) }}

SELECT
    dc.transaction_currency,
    SUM(ft.transaction_amount) AS total_transaction_amount
FROM {{ ref('fact_transactions') }} ft
JOIN {{ ref('dim_card_pii') }} dc ON ft.card_number = dc.card_number
GROUP BY dc.transaction_currency
ORDER BY total_transaction_amount DESC
