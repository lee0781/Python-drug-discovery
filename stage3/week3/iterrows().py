import pandas as pd
import numpy as np

df = pd.read_csv("Stage3/GDSC2-dataset.csv")
df["IC50_uM"]=np.exp(df["LN_IC50"])
df_venet=df[df["DRUG_NAME"]=="Venetoclax"].copy()
df_clean=df_venet[df_venet["Z_SCORE"].abs()<=3].copy()
top10=df_clean.nsmallest(10,"LN_IC50")

print("--Top 10 Venetoclax Sensitive Cell Lines--")
for i, (index,row) in enumerate (top10.iterrows(),start=1):
    name=row["CELL_LINE_NAME"]
    cancer=row["TCGA_DESC"]
    ic50=row["IC50_uM"]
    pathway=row["PATHWAY_NAME"]
    label="ultra" if ic50<0.1 else "sensitive"
    print(f"{i:>2}.{name:<20}{cancer:<8} IC50={ic50:.4f}uM {label}")
