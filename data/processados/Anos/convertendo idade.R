library(dplyr)
library(readr)

# Ler CSV
df <- read_csv(
  "C:/Users/Emanu/Desktop/R_artigo/data/processados/sim_csv/DOCE2012.csv",
  show_col_types = FALSE
)

# Converter idade codificada e criar faixa etária
df <- df %>%
  mutate(
    IDADE = as.integer(IDADE),
    idade_tipo = IDADE %/% 100,
    idade_val  = IDADE %% 100,
    idade_anos = case_when(
      idade_tipo == 4 ~ as.numeric(idade_val),
      idade_tipo == 3 ~ as.numeric(idade_val) / 12,
      idade_tipo == 2 ~ as.numeric(idade_val) / 365.25,
      idade_tipo == 1 ~ as.numeric(idade_val) / (24 * 365.25),
      TRUE ~ NA_real_
    ),
    
    # Criar faixa etária epidemiológica
    faixa_etaria = case_when(
      idade_anos < 1  ~ "<1 ano",
      idade_anos < 5  ~ "1-4",
      idade_anos < 10 ~ "5-9",
      idade_anos < 20 ~ "10-19",
      idade_anos < 30 ~ "20-29",
      idade_anos < 40 ~ "30-39",
      idade_anos < 50 ~ "40-49",
      idade_anos < 60 ~ "50-59",
      idade_anos < 70 ~ "60-69",
      idade_anos < 80 ~ "70-79",
      idade_anos >= 80 ~ "80+",
      TRUE ~ NA_character_
    )
  )

  write_csv(
  df,
  "C:/Users/Emanu/Desktop/R_artigo/data/processados/sim_csv/DOCE2012_com_faixa.csv"
)
