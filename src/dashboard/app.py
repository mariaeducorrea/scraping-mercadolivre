import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('../data/quotes.db')

df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

conn.close()

st.title('Pesquisa de Mercado - Tênis Esportivos no Mercado Livre')

st.subheader('KPIs principais do sistema')


# st.write(df)


col1, col2 , col3 = st.columns(3)

total_items = df.shape[0]
col1.metric(label='Número total de itens', value=total_items)

unique_brands = df['brand'].nunique()
col2.metric(label='Número de Marcas Únicas', value=unique_brands)

average_new_price = df['new_price'].mean()
col3.metric(label='Preço Médio Novo (R$)', value=f'{average_new_price:.2f}')

st.subheader('Marcas mais encontradas até a 10° página.')

col1, col2 = st.columns([4,2])
top_10_pages_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)

st.subheader('Preço médio por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_prices = df[df['new_price'] > 0]
average_price_by_brand = df_non_zero_prices.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)
