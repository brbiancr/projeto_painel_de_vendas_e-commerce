with source as (
    -- DuckDB lê o arquivo Parquet diretamente
    select * from read_parquet('data/trusted\trusted_order_reviews_dataset.parquet')
)

select
    review_id,
    order_id,
    review_score,
    review_creation_date,
    review_answer_timestamp
from source