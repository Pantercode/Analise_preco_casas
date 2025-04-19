import os
import pandas as pd
import kagglehub

# Baixar o dataset
caminho_origem = kagglehub.dataset_download("atharvasoundankar/global-housing-market-analysis-2015-2024")

# Caminho de destino fixo
pasta_de_arquivo = r"C:\Users\marcell.oliveira\Desktop\Global_Housing_Market_Analysis _2015_2024\arquivos"
os.makedirs(pasta_de_arquivo, exist_ok=True)

# Converter os CSVs baixados para Parquet na pasta desejada
for file_name in os.listdir(caminho_origem):
    file_path = os.path.join(caminho_origem, file_name)

    if file_name.lower().endswith(".csv"):
        print(f"Convertendo: {file_name}")
        df = pd.read_csv(file_path)

        arquivo_parquet = file_name.replace(".csv", ".parquet")
        parquet_path = os.path.join(pasta_de_arquivo, arquivo_parquet)

        df.to_parquet(parquet_path, index=False)

print("Conversão concluída. Arquivos Parquet salvos na pasta desejada.")
