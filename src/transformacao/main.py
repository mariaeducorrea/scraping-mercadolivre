#importar o que precisa para o projeto
import pandas as pd
import sqlite3 
from datetime import datetime
import os

#definir o caminho para o arquivo JSONL
df = pd.read_json('../data/data.jsonl', lines=True) 

#setar o pandas para mostrar todas as colunas
pd.options.display.max_columns = None

#adicionar coluna_source com um valor fixo
df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"       #sEMPRE CRIAR ESSA

#adicionar a coluna_data_coleta com a data e hora atuais
df['_data_coleta'] = datetime.now()

#Tratar os valores nulos para colunas numéricas e de texto
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

# Remover os parênteses das colunas `reviews_amount`
df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex=True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

# Tratar os preços como floats e calcular os valores totais
df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100

# Remover as colunas antigas de preços
df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)

# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect('../data/quotes.db')


df['name'] = df['name'].astype(str)

# Salvar o DataFrame no banco de dados SQLite
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()

print(df.head())

# Configurar pandas para mostrar todas as colunas

# Exibir o DataFrame resultante




"""


# Remover as colunas antigas de preços
df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname='your_database_name',  # Substitua pelo nome do seu banco de dados
    user='your_username',          # Substitua pelo seu usuário do PostgreSQL
    password='your_password',      # Substitua pela sua senha do PostgreSQL
    host='localhost',              # Ou o IP do seu servidor PostgreSQL
    port='5432'                    # A porta padrão do PostgreSQL
)

# Salvar o DataFrame no banco de dados PostgreSQL
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()

# Exibir o DataFrame resultante
print(df.head())



"""