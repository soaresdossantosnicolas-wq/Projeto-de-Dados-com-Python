# importas as libs
import pandas  as pd
import plotly.express as px
from pathlib import Path

# Carrega os dados do arquivo CSV
caminho = Path('C:/Users/Nicolas/Documents/dataset/Data/Global_Space_Exploration_Dataset.csv')

df = pd.read_csv(caminho)

# Renomeia as colunas para facilitar o acesso
df = df.rename(columns={  "Budget (in Billion $)": "Budget_Billion",
    "Duration (in Days)": "Duration_Days",
    "Satellite Type": "Satellite_Type"
}) 

# Filtrar apenas colunas válidas e remover valores ausentes
df_box = df[["Satellite_Type", "Budget_Billion", "Duration_Days"]].dropna()

# ---- Boxplot 1 : Oramento por tipo de Satélite ----

fig1 = px.box(
    df_box, 
    x = "Satellite_Type",
    y = "Budget_Billion",
    color = "Satellite_Type",
    points = "outliers",
    title = "Boxplot do Orçamento (em bilhões USD) por Tipo de Satélite")

fig1.update_layout(
    xaxis_title = "Tipo de Satélite",
    yaxis_title = "Orçamento em (Bilhões de USD)",
    template = "plotly_white"
)


fig1.show()



# ---- Boxplot 2 : Duração por tipo de satélite ----

fig2 = px.box(
    df_box,
    x = "Satellite_Type",
    y = "Duration_Days",
    color = "Satellite_Type",
    points = "outliers",
    title = "Boxplot da Duração (em dias) por tipo de Satélite"
)

fig2.update_layout (
    xaxis_title = "Tipo de Satélite",
    yaxis_title = "Duração em Dias",
    template = "plotly_white"
)

fig2.show()
