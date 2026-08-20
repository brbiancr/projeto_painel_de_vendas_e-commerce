# 📦 Análise de Vendas E-commerce — Olist

Pipeline completo de dados (ingestão → modelagem → dashboard) sobre o dataset público [Brazilian E-commerce (Olist)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), com foco em prática de modelagem dimensional e DAX no Power BI.

---

## 🚦 Status do projeto

`Em andamento` 

| Etapa | Status |
|---|---|
| Exploração dos dados | ✅ |
| Ingestão (Python) | ✅ |
| Modelagem staging (dbt) | ⬜ |
| Modelagem star schema (dbt) | ⬜ |
| Conexão e modelo no Power BI | ⬜ |
| Medidas DAX | ⬜ |
| Dashboard final | ⬜ |
| README e documentação finalizados | ⬜ |

---

## 🛠️ Tecnologias utilizadas

- **Python** — ingestão e limpeza de dados
- **kagglehub** — download do dataset


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
│   └── 01_exploracao_dados.ipynb      ← kagglehub download + exploração inicial
│
├── ingestion/
|   └── download_data.py    ← kagglehub → converte CSV para Parquet, salva em raw/
│
├── docs/
│   └── entity_relactionshid_diagram.png                ← diagrama do esquema relacional (inicial)
│
└── data/                        
    ├── raw/
    ├── trusted/
    └── refined/
```
---

## ▶️ Como rodar



---

## 📝 Etapas de execução



### Dia 1 — Exploração



## 🧠 Anotações e aprendizados


### Dificuldades encontradas
-

### Decisões técnicas e por quê
-

### Pontos de atenção / coisas que faria diferente
-

### Conceitos que precisei estudar mais a fundo
-

---

