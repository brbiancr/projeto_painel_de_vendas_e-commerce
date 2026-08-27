with sellers as (
    select * from {{ ref('stg_seller') }}
)

select
    -- Cria a surrogate key aplicando hash MD5 no seller_id
    md5(cast(seller_id as varchar)) as seller_key,

    seller_id, 
    seller_city,
    seller_state
from sellers