import argparse
from pathlib import Path
import pickle
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser("score")
parser.add_argument("--model_input", type=str, help="Path of input model")
parser.add_argument("--X_test_data", type=str, help="Path to test data")
parser.add_argument("--score_output", type=str, help="Path of scoring output")

args = parser.parse_args()

print("Hola desde score...")

lines = [
    f"Model path: {args.model_input}",
    f"Test data path: {args.X_test_data}",
    f"Scoring output path: {args.score_output}",
]

for line in lines:
    print(line)


# TODO cargar el modelo real desde el .pkl
model = pickle.load(open(args.model_input, "rb"))
X_test = pd.read_csv(args.X_test_data)

# TODO: realizar el scoring real

y_pred = model.predict(X_test)

np.savetxt(args.score_output, y_pred, fmt="%d")