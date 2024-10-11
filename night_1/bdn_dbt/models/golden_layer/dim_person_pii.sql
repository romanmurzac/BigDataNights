{{ config(
    schema='golden_layer',
    materialized='table'
) }}

WITH staging_data AS (
    SELECT
        personal_number,
        person_name,
        birth_date,
        address,
        phone_number,
        email,
        ip_address
    FROM
        {{ ref('dim_person') }}
)

SELECT
    *
FROM
    staging_data