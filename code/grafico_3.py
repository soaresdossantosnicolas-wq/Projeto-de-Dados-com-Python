import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# CARREGAMENTO DOS DADOS


caminho = Path('C:/Users/Nicolas/Documents/dataset/Data/Global_Space_Exploration_Dataset.csv')
space_dataset = pd.read_csv(caminho)

# Conferir colunas (use se der erro)
# print(space_dataset.columns)


# AGRUPAMENTO POR ANO E TIPO DE SATÉLITE


budget_by_satellite = (
    space_dataset
    .groupby(["Year", "Satellite Type"])["Budget (in Billion $)"]
    .sum()
    .reset_index()
)


# TOP INVESTIDOR POR TIPO DE SATÉLITE


budget_by_country_sat = (
    space_dataset
    .groupby(["Country", "Satellite Type"])["Budget (in Billion $)"]
    .sum()
    .reset_index()
)

top_investidores = (
    budget_by_country_sat
    .sort_values("Budget (in Billion $)", ascending=False)
    .groupby("Satellite Type")
    .head(1)
    .reset_index(drop=True)
)


# PLOT
plt.figure(figsize=(14, 7))
sns.set_style("whitegrid")

satellite_types = budget_by_satellite["Satellite Type"].unique()
palette = sns.color_palette("Set2", len(satellite_types))

for i, sat_type in enumerate(satellite_types):
    data = budget_by_satellite[
        budget_by_satellite["Satellite Type"] == sat_type
    ]

    plt.plot(
        data["Year"],
        data["Budget (in Billion $)"],
        label=sat_type,
        color=palette[i],
        marker="o",
        linewidth=2
    )

    #  Ponto mínimo 
    min_idx = data["Budget (in Billion $)"].idxmin()
    min_row = data.loc[min_idx]

    min_label = f"{int(min_row['Year'])}:\n{min_row['Budget (in Billion $)']:.1f}B"

    plt.text(
        min_row["Year"],
        min_row["Budget (in Billion $)"] - 2.5,
        min_label,
        color=palette[i],
        fontsize=9,
        fontweight="bold",
        ha="center",
        va="top"
    )

    #  Ponto máximo 
    max_idx = data["Budget (in Billion $)"].idxmax()
    max_row = data.loc[max_idx]

    max_label = f"{int(max_row['Year'])}:\n{max_row['Budget (in Billion $)']:.1f}B"

    plt.text(
        max_row["Year"],
        max_row["Budget (in Billion $)"] + 2.5,
        max_label,
        color=palette[i],
        fontsize=9,
        fontweight="bold",
        ha="center",
        va="bottom"
    )


# LAYOUT FINAL


plt.title(
    "Evolução do Orçamento Espacial por Tipo de Satélite\n(Pontos Máximo e Mínimo)",
    fontsize=16,
    weight="bold"
)

plt.xlabel("Ano", fontsize=12)
plt.ylabel("Orçamento (Bilhões de $)", fontsize=12)
plt.legend(title="Tipo de Satélite")
plt.tight_layout()

# plt.savefig(
#     "grafico_evolucao_orcamento_com_extremos.png",
#     dpi=300
# )

plt.show()


# TABELA TOP INVESTIDORES


print("\n📊 País com Maior Investimento por Tipo de Satélite:\n")

print(
    top_investidores.to_string(
        index=False,
        formatters={
            "Budget (in Billion $)": lambda x: f"${x:,.1f}B"
        }
    )
)
