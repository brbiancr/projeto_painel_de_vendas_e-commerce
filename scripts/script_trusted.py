# Directory and environment configuration
import os
import pandas as pd

RAW_DIR = os.path.join(os.getcwd(), "data" "/raw")
PROCESSED_DIR = os.path.join(os.getcwd(), "data" "/trusted")
os.makedirs(PROCESSED_DIR, exist_ok=True)

def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    df["customer_city"] = df["customer_city"].astype(str).str.lower().str.strip()
    df["customer_state"] = df["customer_state"].astype(str).str.upper().str.strip()

    qtd_composta = df.duplicated(subset=['customer_id', 'customer_unique_id']).sum()
    
    if qtd_composta > 0:
        df = df.drop_duplicates(subset=["customer_id", "customer_unique_id"])

    return df

def clean_geolocation(df: pd.DataFrame) -> pd.DataFrame:
    df["geolocation_zip_code_prefix"] = df["geolocation_zip_code_prefix"].astype(str).str.zfill(8)
    df["geolocation_city"] = df["geolocation_city"].astype(str).str.lower().str.strip()
    df["geolocation_state"] = df["geolocation_state"].astype(str).str.upper().str.strip()

    qtd_composta = df.duplicated(subset=['geolocation_zip_code_prefix', 'geolocation_lat', 'geolocation_lng']).sum()
    
    if qtd_composta > 0:
        df = df.drop_duplicates(subset=["geolocation_zip_code_prefix", "geolocation_lat", "geolocation_lng"])

    return df

def clean_order_items(df: pd.DataFrame) -> pd.DataFrame:
    df["shipping_limit_date"] = pd.to_datetime(df["shipping_limit_date"], errors="coerce")

    qtd_composta = df.duplicated(subset=['order_id', 'order_item_id']).sum()
 
    if qtd_composta > 0:
       df = df.drop_duplicates(subset=["order_id", "order_item_id"])

    return df

def clean_order_payments(df: pd.DataFrame) -> pd.DataFrame:
    qtd_duplicadas = df.duplicated().sum()
    
    if qtd_duplicadas > 0:
        df = df.drop_duplicates(subset=["order_id"])

    return df

def clean_order_reviews(df: pd.DataFrame) -> pd.DataFrame:
    date_cols = [
        "review_creation_date",
        "review_answer_timestamp",
    ]
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    qtd_duplicadas_chave = df.duplicated(subset=['order_id']).sum()
    
    if qtd_duplicadas_chave > 0: 
        df = df.sort_values(by="review_answer_timestamp").drop_duplicates(subset=["review_id"], keep="last")

    return df

def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    date_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    df["order_status"] = df["order_status"].astype(str).str.lower().str.strip()

    qtd_composta = df.duplicated(subset=['order_id', 'customer_id']).sum()
    
    if qtd_composta > 0:
        df = df.drop_duplicates(subset=['order_id', 'customer_id'], keep='last')
    

    return df

def clean_products(df: pd.DataFrame) -> pd.DataFrame:

    df["product_category_name"] = df["product_category_name"].astype(str).str.lower().str.strip()

    qtd_duplicadas_chave = df.duplicated(subset=['product_id']).sum()

    if qtd_duplicadas_chave > 0:
        df = df.drop_duplicates(subset=["product_id"])

    return df

def clean_sellers(df: pd.DataFrame) -> pd.DataFrame:

    df["seller_city"] = df["seller_city"].astype(str).str.lower().str.strip()
    df["seller_state"] = df["seller_state"].astype(str).str.upper().str.strip()

    qtd_duplicadas_chave = df.duplicated(subset=['seller_id']).sum()
    
    if qtd_duplicadas_chave > 0:
        df = df.drop_duplicates(subset=["seller_id"])

    return df

def clean_product_category_translations(df: pd.DataFrame) -> pd.DataFrame:

    df["product_category_name"] = df["product_category_name"].astype(str).str.lower().str.strip()
    df["product_category_name_english"] = df["product_category_name_english"].astype(str).str.lower().str.strip()

    qtd_duplicadas_chave = df.duplicated(subset=['product_category_name']).sum()

    if qtd_duplicadas_chave > 0:
        df = df.drop_duplicates(subset=["product_category_name"])

    return df

def run_pipeline():
    # Mapeamento de arquivo de origem para função de limpeza correspondente
    cleaners = {
        "olist_orders_dataset.parquet": clean_orders,
        "olist_order_items_dataset.parquet": clean_order_items,
        "olist_order_payments_dataset.parquet": clean_order_payments,
        "olist_order_reviews_dataset.parquet": clean_order_reviews,
        "olist_products_dataset.parquet": clean_products,
        "olist_geolocation_dataset.parquet": clean_geolocation,
        "olist_customers_dataset.parquet": clean_customers,
        "olist_sellers_dataset.parquet": clean_sellers,
        "product_category_name_translation.parquet": clean_product_category_translations,
    }

    print("Iniciando processo de limpeza e padronização (Camada Trusted)...\n")

    for file_name, clean_fn in cleaners.items():
        raw_path = os.path.join(RAW_DIR, file_name)
        if not os.path.exists(raw_path):
            print(f"Aviso: Arquivo {file_name} não encontrado em {RAW_DIR}")
            continue

        print(f"Limpando: {file_name}...")
        df_raw = pd.read_parquet(raw_path)
        df_clean = clean_fn(df_raw)

        # Salva o arquivo tratado em Parquet
        output_file_name = file_name.replace("olist_", "trusted_")
        dest_path = os.path.join(PROCESSED_DIR, output_file_name)
        df_clean.to_parquet(dest_path, engine="pyarrow", compression="snappy", index=False)
        print(f"  -> Salvo com sucesso em: {dest_path} (Linhas: {len(df_clean):,})\n")

    print("Pipeline de limpeza concluído com sucesso!")

if __name__ == "__main__":
    run_pipeline()