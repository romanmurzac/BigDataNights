{{ config(
    schema='golden_layer',
    materialized='view'
) }}

WITH ranked_transactions AS (
    SELECT 
        dc.card_number, 
        dc.card_provider, 
        SUM(ft.transaction_amount) AS total_transaction_amount,
        RANK() OVER (ORDER BY SUM(ft.transaction_amount) DESC) AS rank
    FROM {{ ref('fact_transactions') }} ft
    JOIN {{ ref('dim_card_pii') }} dc ON ft.card_number = dc.card_number
    GROUP BY dc.card_number, dc.card_provider
)

SELECT
    *
FROM
    ranked_transactions
WHERE
    rank <= 5
