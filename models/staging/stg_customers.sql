with source as (
    -- DuckDB lê o arquivo Parquet diretamente
    select * from read_parquet('data/trusted\trusted_customers_dataset.parquet')
)

select
    customer_id,
    customer_unique_id,
    customer_city,
    customer_state
from source