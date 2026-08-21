with source as (
    -- DuckDB lê o arquivo Parquet diretamente
    select * from read_parquet('../data\trusted\trusted_orders_dataset.parquet')
)

select
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date
from source