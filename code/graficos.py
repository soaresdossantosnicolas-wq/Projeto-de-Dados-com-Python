# importas as libs
import pandas  as pd
import plotly.express as px
from pathlib import Path

# Carrega os dados do arquivo CSV
caminho = Path('C:/Users/Nicolas/Documents/dataset/Data/Global_Space_Exploration_Dataset.csv')

df = pd.read_csv(caminho)
space_dataset = pd.read_csv(caminho)

# Agrupa e soma os orçamentos por país e ano

budget_by_year_country = (
    df
    .groupby(["Year", "Country"], as_index=False)
    .sum()
)

top_5_countries = (
    budget_by_year_country
    .groupby("Country")["Budget (in Billion $)"]
    .sum()
    .nlargest(5)
    .index
    .tolist()
)

budget_top_countries = budget_by_year_country[budget_by_year_country["Country"].isin(top_5_countries)]

# Cria gráfico interativo

fig = px.line(
    budget_top_countries,
    x = "Year",
    y = "Budget (in Billion $)",
    color = "Country",
    markers = True,
    title = "Evolução do Orçamento Espacial (Top 5 países)",
    labels ={
        "Year": "",
        "Budget (in Billion $)": "",
        "Country": "País"
    },
    hover_data ={"Budget (in Billion $)": ":.2f"} # formatação tooltip
)

fig.update_traces(mode ="lines+markers", marker=dict(size=7), hovertemplate=None)
fig.update_layout(hovermode="x unified", width=1200, height=600)

fig.show(renderer="browser")

fig.show()


