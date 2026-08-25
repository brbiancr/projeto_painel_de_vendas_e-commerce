with source as (
    -- DuckDB lê o arquivo Parquet diretamente
    select * from read_parquet('data/trusted\trusted_sellers_dataset.parquet')
)

select
    seller_id,
    seller_city,
    seller_state
from source