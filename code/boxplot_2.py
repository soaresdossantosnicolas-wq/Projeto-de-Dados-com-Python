import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from pathlib import Path

# CARREGAMENTO DOS DADOS
caminho = Path('C:/Users/Nicolas/Documents/dataset/Data/Global_Space_Exploration_Dataset.csv')
space_dataset = pd.read_csv(caminho)

# Style
plt.style.use('seaborn-v0_8-whitegrid')
mpl.rcParams['font.family'] = 'serif'

# Definição de variáveis
col_orcamento = 'Budget (in Billion $)'
space_dataset = space_dataset.dropna(subset=[col_orcamento])

# Cálculos
media = space_dataset[col_orcamento].mean()
minimo = space_dataset[col_orcamento].min()
maximo = space_dataset[col_orcamento].max()

# Quartis e IQR
q1 = space_dataset[col_orcamento].quantile(0.25)
mediana = space_dataset[col_orcamento].quantile(0.50)
q3 = space_dataset[col_orcamento].quantile(0.75)
iqr = q3 - q1

# Plot 
fig, ax = plt.subplots(figsize=(8,6))
ax.boxplot(space_dataset[col_orcamento], vert=False, patch_artist=True,
           boxprops=dict(facecolor='#69b3a2', color='black'),
           medianprops=dict(color='black'),
           flierprops=dict(marker='o', markerfacecolor='red', markersize=5))

ax.set_title('Distribuição do Orçamento por Missão Espacial (2000-2025)', fontsize=14, weight= 'bold')
ax.set_xlabel('Orçamento da Missão (em bilhões de Dólares)', fontsize=12)
ax.set_yticks([])

# Labels para quartis e IQR
ax.text(q1, 0.87,f'Q1:{q1:.2f}', color='purple', ha='center', fontsize=10)
ax.text(mediana, 0.88, f'Mediana (Q2): {mediana:.2f}', color='black', ha='center', fontsize=10)
ax.text(q3, 0.87, f'Q3: {q3:.2f}', color='purple', ha='center', fontsize=10)

# IQR pode Ficar em texto separado
ax.text(maximo*0.6, 1.15, f'IQR (Q3 - Q1): {iqr:.2f}', color='brown', fontsize=12, weight='bold')

plt.tight_layout()
plt.subplots_adjust(bottom=0.25, top=0.85)
plt.savefig("boxplot_orcamento_missoes_quartis.png", dpi=300)
plt.show()

