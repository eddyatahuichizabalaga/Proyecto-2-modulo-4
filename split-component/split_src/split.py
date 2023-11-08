import argparse
from pathlib import Path
from uuid import uuid4
from datetime import datetime
import os
import pandas as pd
from sklearn.model_selection import train_test_split

# obtener parámetros:
parser = argparse.ArgumentParser("split")
parser.add_argument("--data_filtrado", type=str, help="Path to training data")
parser.add_argument("--X_train", type=str, help="X_train para entrenamiento")
parser.add_argument("--X_test", type=str, help="X_test para validacion")
parser.add_argument("--y_train", type=str, help="y_train para entrenamiento")
parser.add_argument("--y_test", type=str, help="y_test para validacion")

args = parser.parse_args()

print("Hola desde split...")

lines = [
    f"Data filtrado path: {args.data_filtrado}",
    f"X train path: {args.X_train}",
    f"X test path: {args.X_test}",
    f"y train path: {args.y_train}",
    f"y test path: {args.y_test}",
]

print("Parametros: ...")

# imprimir parámetros:

for line in lines:
    print(line)


    
def select_first_file(path):
    """Selects first file in folder, use under assumption there is only one file in folder
    Args:
        path (str): path to directory or file to choose
    Returns:
        str: full path of selected file
    """
    files = os.listdir(path)
    return os.path.join(path, files[0])
# TODO: realizar el entrenamiento del modelo...

# codigo para realizar el split
#carga del data_filtrado a pandas

data = pd.read_csv(select_first_file(args.data_filtrado))

# Dependent vs Independent Variables
X = data.drop(columns=['Potability'])
y = data['Potability']

# Split the dataset into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#guardar salidas
X_train.to_csv(args.X_train, index = False)

X_test.to_csv(args.X_test, index = False)

y_train.to_csv(args.y_train, index = False)

y_test.to_csv(args.y_test, index = False)




