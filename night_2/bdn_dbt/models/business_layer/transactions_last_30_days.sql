{{ config(
    schema='golden_layer',
    materialized='view'
) }}

SELECT
    ft.transaction_number,
    ft.transacted_at,
    ft.transaction_amount,
    dp.person_name,
    dc.card_number
FROM {{ ref('fact_transactions') }} ft
JOIN {{ ref('dim_person_pii') }} dp ON ft.personal_number = dp.personal_number
JOIN {{ ref('dim_card_pii') }} dc ON ft.card_number = dc.card_number
WHERE ft.transacted_at >= CURRENT_DATE - INTERVAL '30 days'
ORDER BY transacted_at DESC