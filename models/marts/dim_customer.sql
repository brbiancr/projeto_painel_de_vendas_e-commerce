with customers as (
    select * from {{ ref('stg_customers') }}
)

select
    -- Cria a surrogate key aplicando hash MD5 no customer_id
    md5(cast(customer_id as varchar)) as customer_key,

    customer_id,
    customer_unique_id,
    customer_city,
    customer_state,
from customers