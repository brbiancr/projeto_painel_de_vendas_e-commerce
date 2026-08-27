with orders as (
    select * from {{ ref('stg_orders') }}
),

order_items as (
    select * from {{ ref('stg_order_items') }}
),

reviews as (
    -- Agrega os reviews caso um pedido tenha múltiplos registros de avaliação
    select
        order_id,
        avg(review_score)::numeric(3, 2) as review_score
    from {{ ref('stg_order_reviews') }}
    group by order_id
)

select
    -- PK / FK Composta da Fato
    md5(cast(i.order_id as varchar)) as order_key,
    i.order_item_id,

    -- Chaves Estrangeiras (FKs para as Dimensões)
    md5(cast(o.customer_id as varchar)) as customer_key,
    md5(cast(i.product_id as varchar)) as product_key,
    md5(cast(i.seller_id as varchar)) as seller_key,
    
    -- FK para dim_date (Data da compra no formato YYYYMMDD)
    cast(strftime(cast(o.order_purchase_timestamp as date), '%Y%m%d') as integer) as date_key_order,
    
    -- FK para dim_date (Data da entrega no formato YYYYMMDD, null se ainda não entregue)
    case 
        when o.order_delivered_customer_date is not null 
        then cast(strftime(cast(o.order_delivered_customer_date as date), '%Y%m%d') as integer)
        else null 
    end as date_key_entrega,

    -- FK para dim_order_status (Hash do status)
    md5(cast(o.order_status as varchar)) as status_key,

    i.price,
    
    -- Cálculo: dias de entrega (compra até entrega real)
    case 
        when o.order_delivered_customer_date is not null 
        then date_diff('day', cast(o.order_purchase_timestamp as date), cast(o.order_delivered_customer_date as date))
        else null 
    end as dias_entrega,
    
    -- Cálculo: dias de atraso (0 se entregue no prazo ou antes)
    case 
        when o.order_delivered_customer_date is not null 
             and cast(o.order_delivered_customer_date as date) > cast(o.order_estimated_delivery_date as date)
        then date_diff('day', cast(o.order_estimated_delivery_date as date), cast(o.order_delivered_customer_date as date))
        when o.order_delivered_customer_date is not null 
        then 0
        else null 
    end as dias_atraso,

    r.review_score,
    i.freight_value

from order_items i
inner join orders o 
    on i.order_id = o.order_id
left join reviews r 
    on i.order_id = r.order_id