# import vowpalwabbit as vp
import pandas as pd
from sklearn.model_selection import train_test_split
# from vowpalwabbit.dftovw import DFtoVW
import re
# from VMLogParser import VWLogParser
import subprocess
import numpy as np

# csv preprocessing
df = pd.read_csv("spam_ham_dataset.csv")
all_cols = list(df)
df[all_cols] = df[all_cols].astype('str')
df["label_num"] = df["label_num"].astype(int)
df["label_num"] = df["label_num"].replace(0, -1)
df["text"] = df["text"].apply(lambda x: re.sub(r'\r\n', ' ', x))
df["text"] = df["text"].apply(lambda x: re.sub(r'Subject:', '', x))
df["text"] = df["text"].apply(lambda x: re.sub(r':', '', x))
df_dump = df[["text", "label_num"]]

# uncomment to save fixed csv
# df_dump.to_csv("spam_fixed.csv")

# data splitting
df_train, df_test = train_test_split(df_dump, test_size=0.1)
df_train.to_csv("spam_train.csv", header=True, index=False)
df_test.to_csv("spam_test.csv", header=True, index=False)

# uncomment for debugging - show df and its types
# print(df_test)
# print(df.dtypes)

# vowpal running
vw_train = "spam_train_vw2.txt"
vw_test = "spam_test_vw2.txt"
vw_model = "model2.vw"
vw_preds = "preds_vw2.txt"

# csv to vw format
cmds = [
    f'python csv2vw.py spam_train.csv --label label_num',
    f"python csv2vw.py spam_test.csv --label label_num"
]
cmds_vw = [
    f"vw -d {vw_train} -f {vw_model}",
    f"vw -d {vw_test} -i {vw_model} -p {vw_preds} --binary"
]

for cmd, file in zip(cmds, [vw_train, vw_test]):
    with open(file, "w") as f:
        subprocess.run(cmd.split(), stdout=f)
for cmd in cmds_vw:
    subprocess.run(cmd.split())

# evaluate
vals = pd.read_csv("spam_test.csv")["label_num"].astype(int).to_numpy()
vals[vals == 0] = -1
with open(vw_preds, 'r') as fh:
    pred = np.array([int(val.strip()) for val in fh])

tp = ((vals == 1) & (pred == 1)).sum()
tn = ((vals == -1) & (pred == -1)).sum()
fp = ((vals == -1) & (pred == 1)).sum()
fn = ((vals == 1) & (pred == -1)).sum()

print("\n>>>> Evaluation:")
print(f"Accuracy = {(vals == pred).sum() / len(pred)}")
print(f"Precision = {tp / (tp + fp)}")
print(f"Recall = {tp / (tp + fn)}")
