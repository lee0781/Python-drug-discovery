import pandas as pd
import numpy as np

df=pd.read_csv("Stage3/GDSC2-dataset.csv")
print(df.shape)
print(df.columns.tolist())
print(df.head())
df["IC50_uM"]=np.exp(df["LN_IC50"])
print(df["IC50_uM"].mean().round(2))