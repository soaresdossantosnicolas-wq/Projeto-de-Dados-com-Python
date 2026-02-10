# %%
# importas as libs
import pandas  as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path

# Carrega os dados do arquivo CSV
caminho = Path('C:/Users/Nicolas/Documents/dataset/Data/Global_Space_Exploration_Dataset.csv')

df = pd.read_csv(caminho)
space_dataset = pd.read_csv(caminho)

# Agrupa os orçamentos por ano e tipo de satélite
budget_by_satellite = (
    space_dataset.groupby(["Year", "Satellite Type"])
    ["Budget (in Billion $)"].sum().reset_index()
)

# Encontra país que mais investiu em cada tipo de satélite
budget_by_country_sat = (
    space_dataset.groupby(["Satellite Type", "Country"])
    ["Budget (in Billion $)"].sum().reset_index()
)
top_investidores = budget_by_country_sat.loc[budget_by_country_sat.groupby("Satellite Type")["Budget (in Billion $)"].idxmax()]

# ---- Gráfico de Linha ----
fig = make_subplots(
    rows = 2, cols = 1,
    row_heights = [0.7,0.3],
    shared_xaxes = False,
    vertical_spacing = 0.05,
    specs = [[{"type": "scatter"}], [{"type": "table"}]]
)

# Paletas de cores para cada tipo de Satélite

palette = px.colors.qualitative.Set2
satellite_types = budget_by_satellite["Satellite Type"].unique()
color_map = dict(zip(satellite_types, palette))

# Adiciona uma linha por tipo de Satélite
for sat_type in satellite_types:
    sat_data = budget_by_satellite[budget_by_satellite["Satellite Type"] == sat_type]

    fig.add_trace(
        go.Scatter(
            x = sat_data["Year"],
            y = sat_data["Budget (in Billion $)"],
            mode = "lines+markers",
            name = sat_type,
            marker = dict(color=color_map[sat_type])
        ),
        row = 1, col = 1
    )

# ---- Tabela Inferior ----
fig.add_trace(
    go.Table(
        header = dict(values = ["Tipo de Satélite", "País com maior investimento", "Total Investido"],
                      fill_color = "lightgray", align = "center", font = dict(size = 14)),
                      cells = dict(
                          values = [
                              top_investidores["Satellite Type"],
                              top_investidores["Country"],
                              top_investidores["Budget (in Billion $)"]  .apply(lambda x: f"${x:.1f}B")

                          ],
                          align = "center", font = dict(size=12)
                      )
    ),
    row = 2, col = 1
)

# ---- Layout final ----
fig.update_layout(
    title = "🛰️ Evolução do Orçamento Espacial por Tipo de Satélite + Top Investidores",
    height = 800,
    width = 1200,
    legend_title = "Tipo de Satélite",
    hovermode = "x unified"
)

fig.update_yaxes(title_text = "Orçamento (Bilhões de $)", row  = 1, col = 1)

fig.show(renderer="browser")
fig.show()