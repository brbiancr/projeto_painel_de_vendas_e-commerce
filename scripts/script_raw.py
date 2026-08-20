import os
import kagglehub
import pandas as pd

# 1. Diretório de destino local no seu projeto
DEST_DIR = os.path.join(os.getcwd(), "data", "raw")
os.makedirs(DEST_DIR, exist_ok=True)

# 2. Download do dataset do Kaggle (baixa na pasta de cache)
print("Baixando dataset da Olist...")
download_path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
print(f"Dataset baixado no cache: {download_path}")

# 3. Converter cada CSV para Parquet
print("Iniciando conversão de CSV para Parquet...")
for file_name in os.listdir(download_path):
    if file_name.endswith(".csv"):
        csv_path = os.path.join(download_path, file_name)
        
        # Define o nome de saída trocando .csv por .parquet
        parquet_file_name = file_name.replace(".csv", ".parquet")
        parquet_path = os.path.join(DEST_DIR, parquet_file_name)

        print(f"Convertendo: {file_name} -> {parquet_file_name}...")
        
        # Leitura do CSV e gravação em Parquet (comprimido em snappy)
        df = pd.read_csv(csv_path)
        df.to_parquet(parquet_path, engine="pyarrow", compression="snappy", index=False)

print(f"\nTodos os arquivos foram salvos em formato Parquet em: {DEST_DIR}")