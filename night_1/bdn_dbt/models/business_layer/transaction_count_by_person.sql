{{ config(
    schema='golden_layer',
    materialized='view'
) }}

SELECT
    dp.person_name,
    COUNT(ft.transaction_number) AS transaction_count
FROM {{ ref('fact_transactions') }} ft
JOIN {{ ref('dim_person_pii') }} dp ON ft.personal_number = dp.personal_number
GROUP BY dp.person_name
ORDER BY transaction_count DESC
