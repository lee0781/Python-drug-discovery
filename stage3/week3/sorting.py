import pandas as pd
import numpy as np

df = pd.read_csv("Stage3/GDSC2-dataset.csv")
df["IC50_uM"]=np.exp(df["LN_IC50"])
df_venet=df[df["DRUG_NAME"]=="Venetoclax"].copy()
df_clean=df_venet[df_venet["Z_SCORE"].abs()<=3].copy()

#sorting by ic50
df_sorted=df_clean.sort_values("LN_IC50")
print("==Top 5 most sensitive==")
print(df_sorted[["CELL_LINE_NAME","TCGA_DESC","IC50_uM"]].head())

#smallest
top10=df_clean.nsmallest(10,"LN_IC50")
print("Top 10 most sensitive cell lines:")
print(top10[["CELL_LINE_NAME","TCGA_DESC","IC50_uM"]].round(4))

#top 5 most resistant
bottom5=df_clean.nlargest(5,"LN_IC50")
print("top 5 most resistant")
print(bottom5[["CELL_LINE_NAME","TCGA_DESC","IC50_uM"]].round(2))
