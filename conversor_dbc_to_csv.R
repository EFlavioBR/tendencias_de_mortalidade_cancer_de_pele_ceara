library(read.dbc)
library(readr)
library(tools)

pasta_dbc <- "data/brutos/sim"
pasta_csv <- "data/processados/sim_csv"

dir.create(pasta_csv, showWarnings = FALSE, recursive = TRUE)

arquivos <- list.files(pasta_dbc,
                       pattern = "\\.dbc$",
                       full.names = TRUE,
                       ignore.case = TRUE)

cat("Encontrados", length(arquivos), "arquivos DBC\n")

for (caminho in arquivos) {

  cat("Convertendo:", basename(caminho), "\n")

  df <- read.dbc::read.dbc(caminho)

  nome_base <- file_path_sans_ext(basename(caminho))
  caminho_saida <- file.path(pasta_csv, paste0(nome_base, ".csv"))

  readr::write_csv(df, caminho_saida)

  cat("✔ Salvo em:", caminho_saida, "\n\n")
}

cat("Conversão finalizada.\n")