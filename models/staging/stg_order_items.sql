with source as (
    -- DuckDB lê o arquivo Parquet diretamente
    select * from read_parquet('../data\trusted\trusted_order_items_dataset.parquet')
)

select
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value
from source