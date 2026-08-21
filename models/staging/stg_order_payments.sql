with source as (
    -- DuckDB lê o arquivo Parquet diretamente
    select * from read_parquet('../data\trusted\trusted_order_payments_dataset.parquet')
)

select
    order_id,
    payment_sequential,
    payment_type,
    payment_installments,
    payment_value
from source