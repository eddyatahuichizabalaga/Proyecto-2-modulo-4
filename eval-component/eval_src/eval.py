import argparse
from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np
import os
from sklearn.metrics import classification_report

parser = argparse.ArgumentParser("score")
parser.add_argument("--scoring_result", type=str, help="Path of scoring result")
parser.add_argument("--y_test", type=str, help="Path of y test")
parser.add_argument("--eval_output", type=str, help="Path of output evaluation result")

args = parser.parse_args()

print("Hola desde eval...")

lines = [
    f"Scoring result path: {args.scoring_result}",
    f"y test path: {args.y_test}",
    f"Evaluation output path: {args.eval_output}",
]

for line in lines:
    print(line)

    
# TODO: evalua el scoring real

y_test = pd.read_csv(args.y_test)


y_pred = np.loadtxt(args.scoring_result, dtype=int)

report = classification_report(y_test, y_pred, target_names=["Not Potable", "Potable"], output_dict=True)


df_rep = pd.DataFrame(report).transpose()



df_rep.to_csv(os.path.join(args.eval_output, "metricas.csv"),index = False)