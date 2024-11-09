{{ config(
    schema='golden_layer',
    materialized='view'
) }}

SELECT
    ft.from_country,
    ROUND(AVG(ft.transaction_amount), 2) AS avg_transaction_amount
FROM
    {{ ref('fact_transactions') }} ft
GROUP BY ft.from_country
ORDER BY avg_transaction_amount DESC
