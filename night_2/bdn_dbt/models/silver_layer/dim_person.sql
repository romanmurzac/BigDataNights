{{ config(
    schema='silver_layer',
    materialized='table'
) }}

SELECT
    personal_number,
    person_name,
    birth_date,
    address,
    phone_number,
    email,
    ip_address
FROM
    {{ source('bronze_layer', 'raw_data') }}
