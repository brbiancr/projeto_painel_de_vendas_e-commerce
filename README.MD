# 📦 Análise de Vendas E-commerce — Olist

Pipeline completo de dados (ingestão → modelagem → dashboard) sobre o dataset público [Brazilian E-commerce (Olist)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), com foco em prática de modelagem dimensional e DAX no Power BI.

---

## 🚦 Status do projeto

`Finalizado` 

| Etapa | Status |
|---|---|
| Exploração dos dados | ✅ |
| Ingestão (Python) | ✅ |
| Modelagem staging (dbt) | ✅ |
| Modelagem star schema (dbt) | ✅ |
| Conexão e modelo no Power BI | ✅ |
| Medidas DAX | ✅ |
| Dashboard final | ✅ |
| README e documentação finalizados | ✅ |

---

## 🛠️ Tecnologias utilizadas

- **Python** — ingestão e limpeza de dados
- **kagglehub** — download do 
- **DuckBD** - datawarehouse local
- **dbt-core** - transformação e modelagem dimensional
- **Power BI Desktop** — dashboard e medidas DAX


---

## 🏗️ Arquitetura
```
Kaggle (Olist dataset)
        │
        ▼
  Ingestão (Python) ──► Parquet (raw)
        │
        ▼
     dbt staging ──► dbt marts (star schema)
        │
        ▼
      DuckDB (warehouse)
        │
        ▼
   Power BI (modelo + DAX)
```

---

## 📁 Estrutura do repositório

```

olist-ecommerce-analytics/
├── README.md
├── .gitignore
├── requirements.txt
|
├── notebooks/      ← testes
│
├── scripts/
|   ├── script_raw.py       ← kagglehub → converte CSV para Parquet, salva em raw/
|   ├── script_trusted.py       ← limpeza e tratamento dos dados 
|   └── script_refined.py       ← modelo estrela
│
├── docs/
│   ├── entity_relactionshid_diagram.png                ← diagrama do esquema relacional (inicial)
|   └── star_schema_diagram         ← diagrama do modelo estrela
│
├── models/
|   ├── staging/
│   └── marts/
|
└── data/                        
    ├── raw/
    ├── trusted/
    ├── refined/
    └── duckdb/
```
---

## ▶️ Como rodar
```
# 1. Ambiente
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt

# 2. Ingestão
python script/script_raw.py

# 3. Transformação
python script/script_trusted.py

# 4. DBT
dbt debug --profiles-dir .  
dbt run --profiles-dir .  
dbt test --profiles-dir .
```
---