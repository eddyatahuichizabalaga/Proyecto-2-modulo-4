import argparse
from pathlib import Path
from uuid import uuid4
from datetime import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# obtener parámetros:
parser = argparse.ArgumentParser("train")
parser.add_argument("--data", type=str, help="Data original")
parser.add_argument("--data_filtrado", type=str, help="Data a entrenar")
parser.add_argument("--imagen_correlacion", type=str, help="imagen")

args = parser.parse_args()

print("Hola desde proceso...")

lines = [
    f"Data path: {args.data}",
    f"Data filtrado path: {args.data_filtrado}",
    f"Imagen correlacion path: {args.imagen_correlacion}",
]

print("Parametros: ...")

# imprimir parámetros:

for line in lines:
    print(line)


# filtrado de paquetes

data = pd.read_csv(args.data)
data = data.fillna(data.mean())


# Calculate the correlation matrix
correlation_matrix = data.corr(method='pearson')

# Create a heatmap
fig, ax = plt.subplots(figsize = (20, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, linecolor='black', vmin=-1, vmax=1,cbar=False)
ax.set_yticklabels(ax.get_yticklabels(), rotation="horizontal")
plt.title('Correlation Heatmap')

#guardar la imagen
#

plt.savefig(os.path.join(args.imagen_correlacion, "correlacion.jpg"), dpi = 300, bbox_inches='tight', pad_inches=0.0)

#guardar el data filtrado

data.to_csv(os.path.join(args.data_filtrado, "data_filtrado.csv"), index=False)


