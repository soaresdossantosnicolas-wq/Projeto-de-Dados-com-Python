import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# CARREGAMENTO DOS DADOS
caminho = Path('C:/Users/Nicolas/Documents/dataset/Data/Global_Space_Exploration_Dataset.csv')
space_dataset = pd.read_csv(caminho)

# Style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('pastel')

# Define colunas categóricas
categorias = {
    'Country': "Número de missões por País",
    'Mission Type': "Frequência por Tipo de Missão",
    'Satellite Type': "Freqência por Tipo de Satélite",
    'Technology Used': "Frequência por Tipo de Tecnologia"
}

# Plot dos Gráficos
fig, axes = plt.subplots(2, 2, figsize=(16,10))
axes = axes.flatten()

for i, (coluna, titulo) in enumerate(categorias.items()):
    top_categorias = space_dataset[coluna].value_counts().head(10)
    sns.barplot(x=top_categorias.values, y=top_categorias.index, ax=axes[i])
    axes[i].set_title(titulo,fontsize=13,weight='bold')
    axes[i].set_xlabel('Número de Registros')
    axes[i].set_ylabel("")

plt.tight_layout()    
plt.savefig('categorias_espaciais.png', dpi=300)
plt.show()
