import argparse
from pathlib import Path
from uuid import uuid4
from datetime import datetime
import os
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression

# obtener parámetros:
parser = argparse.ArgumentParser("train_LR")
parser.add_argument("--X_train", type=str, help="Path to X_training data")
parser.add_argument("--y_train", type=str, help="Path to y_training data")
parser.add_argument("--model_output", type=str, help="Path of output model")
parser.add_argument("--model_pkl", type=str, help="modelo pkl")

args = parser.parse_args()

print("Hola desde train Logistic_Regression...")

lines = [
    f"Training data path: {args.X_train}",
    f"Max epocs: {args.y_train}",
    f"Model output path: {args.model_output}",
    f"Model pkl: {args.model_pkl}",
]

print("Parametros: ...")

# imprimir parámetros:

for line in lines:
    print(line)

# TODO: realizar el entrenamiento del modelo...

# Create a binary classification model (Logistic Regression in this case)
model = LogisticRegression()
X_train = pd.read_csv(args.X_train)
y_train = pd.read_csv(args.y_train)
# Train the model on the training data
model.fit(X_train, y_train)


# guardar modelo en memoria
pickle.dump(model, open(args.model_output, "wb"))

#para exportar

pickle.dump(model, open(os.path.join(args.model_pkl, "modelo.pkl"), "wb"))