with date_range as (
    -- 1. Encontra a menor e a maior data considerando compras e entregas
    select 
        cast(min(least(
            cast(order_purchase_timestamp as date),
            coalesce(cast(order_delivered_customer_date as date), cast(order_purchase_timestamp as date))
        )) as date) as min_date,
        cast(max(greatest(
            cast(order_purchase_timestamp as date),
            coalesce(cast(order_delivered_customer_date as date), cast(order_purchase_timestamp as date)),
            coalesce(cast(order_estimated_delivery_date as date), cast(order_purchase_timestamp as date))
        )) as date) as max_date
    from {{ ref('stg_orders') }}
),

calendar as (
    -- 2. DuckDB gera a série contínua dia a dia entre o min e o max
    select 
        unnest(generate_series(min_date, max_date, interval '1 day'))::date as complete_date
    from date_range
)

select
    -- PK da dimensão de data no formato inteiro YYYYMMDD (ex: 20180105)
    cast(strftime(complete_date, '%Y%m%d') as integer) as date_key,
    
    complete_date,
    extract(year from complete_date)::integer as year,
    extract(month from complete_date)::integer as month,
    extract(day from complete_date)::integer as day,
    
    -- Dia da semana (1 = Segunda-feira, 7 = Domingo)
    extract(isodow from complete_date)::integer as day_week,

    strftime(complete_date, '%B') as month_name,
    
    -- Indicador de fim de semana (True se sábado ou domingo)
    case 
        when extract(isodow from complete_date) in (6, 7) then true 
        else false 
    end as is_weekend

from calendar
order by complete_date