# 📊 Tendências de Mortalidade por Câncer de Pele no Ceará (2011–2021)

Repositório de apoio ao artigo científico sobre a análise da mortalidade por câncer de pele (Melanoma C43 e Não-Melanoma C44) no estado do Ceará, Brasil, no período de 2011 a 2021.

---

## 📋 Sobre o Estudo

Este estudo analisa os óbitos por câncer de pele registrados no **Sistema de Informações sobre Mortalidade (SIM/DATASUS)** para o estado do Ceará, investigando tendências temporais, perfil sociodemográfico das vítimas e taxas de mortalidade ajustadas pela população estimada pelo IBGE.

**Período de análise:** 2011 – 2021  
**Fonte dos dados:** DATASUS (SIM) e IBGE (estimativas populacionais)  
**Tipos de neoplasia:** Melanoma (CID-10: C43) e Não-Melanoma (CID-10: C44)

---

## 🗂️ Estrutura do Repositório

```
📦 tendencias_de_mortalidade_cancer_de_pele_ceara
 ┣ 📂 data/
 ┃ ┣ 📂 bruto/
 ┃ ┃ ┣ DOCE2010.DBC
 ┃ ┃ ┣ DOCE2011.DBC
 ┃ ┃ ┣ ...
 ┃ ┃ ┗ DOCE2024.DBC                             # Arquivos brutos do SIM/DATASUS
 ┃ ┗ 📂 processados/
 ┃   ┣ 📂 Anos/                                 # Dados separados por ano
 ┃   ┣ microdados_cancer_pele_limpos_ceara.csv  # Microdados limpos
 ┃   ┣ obitos_c43_c44_por_ano.csv               # Óbitos agregados por ano e tipo
 ┃   ┣ obitos_pele_ceara_2011_2021.csv          # Base final filtrada (2011–2021)
 ┃   ┗ pop_estimada_IBGE_CE - Página1.csv       # Estimativas populacionais IBGE
 ┣ 📂 images/
 ┃   ┣ grafico_01_taxa_ajustada.png
 ┃   ┣ grafico_02_proporcao.png
 ┃   ┣ grafico_03_idade_boxplot.png
 ┃   ┣ grafico_04_tendencia_C44.png
 ┃   ┣ grafico_05_tendencia_C43.png
 ┃   ┣ grafico_06_variacao_anual.png
 ┃   ┣ grafico_07_faixa_etaria.png
 ┃   ┣ grafico_08_sexo.png
 ┃   ┣ grafico_09_evolucao_sexo.png
 ┃   ┣ grafico_10_raca_cor_barras.png
 ┃   ┣ grafico_10_raca_cor_comparativo.png
 ┃   ┗ grafico_11_projecao_10_anos.png
 ┣ 📄 conversor_dbc_to_csv.R                    # Script R para converter .DBC em .CSV
 ┣ 📄 processar_dados.py                        # Script Python de limpeza e filtragem
 ┣ 📓 gráficos.ipynb                            # Notebook com geração de todos os gráficos
 ┗ 📄 README.md
```

---

## ⚙️ Como Reproduzir

### 1. Clone o repositório

```bash
git clone https://github.com/EFlavioBR/tendencias_de_mortalidade_cancer_de_pele_ceara.git
cd tendencias_de_mortalidade_cancer_de_pele_ceara
```

### 2. Instale as dependências

**Python:**
```bash
pip install pandas numpy matplotlib seaborn scipy
```

**R** (para conversão dos arquivos .DBC):
```r
install.packages("read.dbc")
```

### 3. Converta os arquivos brutos (.DBC → .CSV)

Execute o script R `conversor_dbc_to_csv.R` para converter os arquivos brutos do DATASUS.

### 4. Execute o processamento dos dados

```bash
python processar_dados.py
```

> Gera o arquivo `obitos_pele_ceara_2011_2021.csv` com os registros filtrados para o período 2011–2021.

### 5. Gere os gráficos

Abra o `gráficos.ipynb` no Jupyter e execute todas as células em ordem.

---

## 📈 Gráficos Gerados

| # | Arquivo | Descrição |
|---|---------|-----------|
| 01 | `grafico_01_taxa_ajustada.png` | Taxa de mortalidade ajustada por 100 mil habitantes |
| 02 | `grafico_02_proporcao.png` | Proporção de óbitos por Melanoma e Não-Melanoma |
| 03 | `grafico_03_idade_boxplot.png` | Distribuição da idade ao óbito por ano |
| 04 | `grafico_04_tendencia_C44.png` | Curva de tendência — Não-Melanoma (C44) |
| 05 | `grafico_05_tendencia_C43.png` | Curva de tendência — Melanoma (C43) |
| 06 | `grafico_06_variacao_anual.png` | Variação percentual anual de óbitos |
| 07 | `grafico_07_faixa_etaria.png` | Óbitos por faixa etária |
| 08 | `grafico_08_sexo.png` | Óbitos segundo o sexo |
| 09 | `grafico_09_evolucao_sexo.png` | Evolução dos óbitos por sexo — Não-Melanoma (C44) |
| 10a | `grafico_10_raca_cor_barras.png` | Óbitos por raça/cor — Não-Melanoma (C44) |
| 10b | `grafico_10_raca_cor_comparativo.png` | Óbitos por raça/cor — C43 vs C44 |
| 11 | `grafico_11_projecao_10_anos.png` | Projeção de mortalidade para 2022–2031 |

---

## 🛠️ Tecnologias Utilizadas

- Python 3.14 — processamento e visualização de dados
- R — conversão dos arquivos .DBC do DATASUS
- pandas, numpy, matplotlib, seaborn, scipy

---

## 👤 Autor

**Emanuell Flávio**  
GitHub: [@EFlavioBR](https://github.com/EFlavioBR)

---

## 📌 Observações

- Os arquivos `.DBC` brutos são os originais obtidos no portal [DATASUS](https://datasus.saude.gov.br/).
- O script `processar_dados.py` filtra automaticamente os registros para o período **2011–2021**, descartando entradas com datas inconsistentes comuns nas bases do SIM.
- Os dados de 2022, 2023 e 2024 estão presentes nos arquivos brutos mas **não são utilizados na análise** por ausência de estimativas populacionais compatíveis para o cálculo das taxas de mortalidade.
