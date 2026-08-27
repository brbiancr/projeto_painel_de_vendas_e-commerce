from pathlib import Path
import duckdb

# Define os caminhos do projeto
BASE_DIR = Path(__file__).resolve().parent.parent
DUCKDB_PATH = BASE_DIR / "data" / "duckdb" / "olist.duckdb"
REFINED_DIR = BASE_DIR / "data" / "refined"

# Cria o diretório de destino caso não exista
REFINED_DIR.mkdir(parents=True, exist_ok=True)

# Lista apenas as tabelas do Star Schema (Marts)
TABLES_TO_EXPORT = [
    "dim_customer",
    "dim_date",
    "dim_order",
    "dim_order_status",
    "dim_product",
    "dim_seller",
    "fct_order",
    "fct_payment"
]

def export_refined():
    if not DUCKDB_PATH.exists():
        raise FileNotFoundError(f"Banco não encontrado em: {DUCKDB_PATH}")

    con = duckdb.connect(str(DUCKDB_PATH), read_only=True)
    print("Iniciando exportação da camada Refined (Parquet)...")

    for table in TABLES_TO_EXPORT:
        output_file = REFINED_DIR / f"{table}.parquet"
        
        # Consulta direta no schema main
        query = f"""
            COPY (SELECT * FROM main.{table}) 
            TO '{output_file.as_posix()}' 
            (FORMAT PARQUET, COMPRESSION SNAPPY);
        """
        con.execute(query)
        print(f"Tabela '{table}' exportada com sucesso -> {output_file.name}")

    con.close()
    print("\nExportação concluída com sucesso!")

if __name__ == "__main__":
    export_refined()