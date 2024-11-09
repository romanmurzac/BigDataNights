{{ config(
    schema='golden_layer',
    materialized='table'
) }}

WITH staging_data AS (
    SELECT
        personal_number,
        CONCAT(SUBSTRING(person_name, 1, 1), '***') AS masked_person_name,
        birth_date,
        CONCAT('***', SUBSTRING(address, LENGTH(address) - POSITION(',' IN REVERSE(address)) + 1, LENGTH(address))) AS masked_address,
        CONCAT('***-***-', RIGHT(phone_number, 4)) AS masked_phone_number,
        CONCAT('***@', SUBSTRING(email, POSITION('@' IN email) + 1)) AS masked_email,
        CONCAT('***.***.***.', RIGHT(ip_address, 1)) AS masked_ip_address
    FROM
        {{ ref('dim_person') }}
)

SELECT
    *
FROM
    staging_data