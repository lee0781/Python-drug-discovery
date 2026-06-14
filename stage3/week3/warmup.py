import pandas as pd
import numpy as np
df=pd.read_csv("Stage3/GDSC2-dataset.csv")

df_venet=df[df["DRUG_NAME"]=="Venetoclax"].copy()
df_venet_group=df_venet.groupby("TCGA_DESC")["LN_IC50"].mean().reset_index()
top5=df_venet_group.sort_values("LN_IC50").head(5)
print(top5)