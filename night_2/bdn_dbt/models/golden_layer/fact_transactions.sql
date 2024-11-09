{{ config(
    schema='golden_layer',
    materialized='table'
) }}

WITH staging_data AS (
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
        {{ ref('fact_transaction') }}
)

SELECT
    *
FROM
    staging_data