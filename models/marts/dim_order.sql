with orders as (
    select * from {{ ref('stg_orders') }}
)

select
    -- Cria a surrogate key aplicando hash MD5 no order_id
    md5(cast(order_id as varchar)) as order_key,

    order_id
from orders