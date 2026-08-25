with source as (
    -- DuckDB lê o arquivo Parquet diretamente
    select * from read_parquet('data/trusted\trusted_products_dataset.parquet')
)

select
    product_id,
    product_category_name,
from source