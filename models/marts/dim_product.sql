with products as (
    select * from {{ ref('stg_products') }}
)

select
    -- Cria a surrogate key aplicando hash MD5 no product_id
    md5(cast(product_id as varchar)) as product_key,

    product_id
    product_category_name
from products