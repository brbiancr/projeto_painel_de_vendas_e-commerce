# 📦 Análise de Vendas E-commerce — Olist

Pipeline completo de dados (ingestão → modelagem → dashboard) sobre o dataset público [Brazilian E-commerce (Olist)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), com foco em prática de modelagem dimensional e DAX no Power BI.

---

## 🚦 Status do projeto

`Em andamento` 

| Etapa | Status |
|---|---|
| Exploração dos dados | ✅ |
| Ingestão (Python) | ✅ |
| Modelagem staging (dbt) | ✅ |
| Modelagem star schema (dbt) | ⬜ |
| Conexão e modelo no Power BI | ⬜ |
| Medidas DAX | ⬜ |
| Dashboard final | ⬜ |
| README e documentação finalizados | ⬜ |

---

## 🛠️ Tecnologias utilizadas

- **Python** — ingestão e limpeza de dados
- **kagglehub** — download do 
- **DuckBD** - datawarehouse local
- **dbt-core** - transformação e modelagem dimensional


---

## 🏗️ Arquitetura


---

## 📁 Estrutura do repositório

```

olist-ecommerce-analytics/
├── README.md
├── .gitignore
├── requirements.txt
|
├── notebooks/
│   ├── 01_raw.ipynb      ← kagglehub download + exploração inicial
|   ├── 02_trusted
|   └── 03_duckdb_test.ipynb
│
├── scripts/
|   ├── script_raw.py       ← kagglehub → converte CSV para Parquet, salva em raw/
|   └── script_trusted.py       ← limpeza e tratamento dos dados 
│
├── docs/
│   └── entity_relactionshid_diagram.png                ← diagrama do esquema relacional (inicial)
│
├── models/ staging
│   └── schema.yml
|
└── data/                        
    ├── raw/
    ├── trusted/
    └── refined/
```
---

## ▶️ Como rodar

---