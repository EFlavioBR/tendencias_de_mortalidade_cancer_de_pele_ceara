# Importação das bibliotecas necessárias
import pandas as pd
import numpy as np
import glob
import os

# Caminho da pasta onde estão os arquivos CSV processados
caminho_pasta = r"C:\Users\Emanu\Desktop\R_artigo\data\processados\sim_csv"

# Padrão de busca para arquivos CSV que começam com "DOCE"
padrao_busca = os.path.join(caminho_pasta, "DOCE*.csv")
arquivos_csv = glob.glob(padrao_busca)

# Imprime o número de arquivos encontrados
print(f"Encontrados {len(arquivos_csv)} arquivos na pasta.")

# Função para calcular a idade em anos a partir do código de idade
def calcular_idade_anos(idade_cod):
    try:
        idade_str = str(int(idade_cod))
        if len(idade_str) == 3:
            unidade = idade_str[0]
            qtd = int(idade_str[1:])
            if unidade == '4': return qtd          # Dias
            elif unidade == '5': return 100 + qtd  # Anos acima de 100
            else: return 0                         # Outros casos
    except:
        return np.nan
    return np.nan

# Função para extrair o ano da data de óbito
def extrair_ano(dt):
    try:
        dt_str = str(int(dt)).zfill(8)  # Preenche com zeros à esquerda para 8 dígitos
        return int(dt_str[-4:])  # Últimos 4 dígitos são o ano
    except:
        return np.nan

# Lista para armazenar os DataFrames processados
lista_dados = []

# Colunas de interesse dos arquivos CSV
colunas_interesse = ['DTOBITO', 'IDADE', 'SEXO', 'RACACOR', 'CAUSABAS', 'CODMUNRES']

# Loop para processar cada arquivo CSV encontrado
for arquivo in arquivos_csv:
    nome_arquivo = os.path.basename(arquivo)
    print(f"Processando {nome_arquivo}...")
    
    # Lê o arquivo CSV, selecionando apenas as colunas de interesse
    df_temp = pd.read_csv(arquivo, usecols=lambda c: c in colunas_interesse, low_memory=False)
    
    # Filtra os dados para óbitos por câncer de pele (C43 e C44)
    df_pele = df_temp[df_temp['CAUSABAS'].astype(str).str.startswith(('C43', 'C44'))].copy()
    
    if not df_pele.empty:
        # Extrai o ano do óbito
        df_pele['Ano_Obito'] = df_pele['DTOBITO'].apply(extrair_ano)
        # Classifica o tipo de câncer
        df_pele['Tipo_Cancer'] = np.where(df_pele['CAUSABAS'].str.startswith('C43'), 'Melanoma (C43)', 'Não-Melanoma (C44)')
        # Calcula a idade em anos
        df_pele['Idade_Anos'] = df_pele['IDADE'].apply(calcular_idade_anos)
        
        # Mapeia o código de sexo para nome
        df_pele['Sexo_Nome'] = df_pele.get('SEXO', pd.Series([np.nan]*len(df_pele))).map(
            {1: 'Masculino', 2: 'Feminino'}
        ).fillna('Ignorado')
        
        # Mapeia o código de raça/cor para nome
        df_pele['Raca_Nome'] = df_pele.get('RACACOR', pd.Series([np.nan]*len(df_pele))).map(
            {1: 'Branca', 2: 'Preta', 3: 'Amarela', 4: 'Parda', 5: 'Indígena'}
        ).fillna('Ignorado')
        
        # Define faixas etárias
        bins = [-1, 19, 39, 59, 79, 150]
        labels = ['0-19 anos', '20-39 anos', '40-59 anos', '60-79 anos', '80+ anos']
        df_pele['Faixa_Etaria'] = pd.cut(df_pele['Idade_Anos'], bins=bins, labels=labels)
        
        # Adiciona o DataFrame processado à lista
        lista_dados.append(df_pele)

# Se há dados processados, concatena e salva
if len(lista_dados) > 0:
    df_final = pd.concat(lista_dados, ignore_index=True)
    
    # Seleciona as colunas finais
    colunas_finais = ['Ano_Obito', 'CAUSABAS', 'Tipo_Cancer', 'Idade_Anos', 'Faixa_Etaria', 'Sexo_Nome', 'Raca_Nome', 'CODMUNRES']
    df_final = df_final[colunas_finais]
    
    # Caminho para salvar o arquivo final
    caminho_saida = os.path.join(caminho_pasta, "obitos_pele_ceara_2011_2021.csv")
    df_final.to_csv(caminho_saida, index=False, encoding='utf-8')
    
    # Imprime mensagem de sucesso
    print(f"\nSucesso! Foram unidos {len(df_final)} óbitos de pele.")
    print(f"O arquivo final foi salvo em: {caminho_saida}")
else:
    print("Nenhum dado de C43 ou C44 encontrado.")