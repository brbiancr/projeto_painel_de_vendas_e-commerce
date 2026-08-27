with payments as (
    select * from {{ ref('stg_order_payments') }}
)

select
    -- PK / FK: Chave substituta apontando para dim_order / fact_order
    md5(cast(order_id as varchar)) as order_key,
    
    payment_sequential,
    payment_type,
    payment_installments,
    payment_value
from payments