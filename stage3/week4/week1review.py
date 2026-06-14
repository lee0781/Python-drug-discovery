import numpy as np
import pandas as pd

#1
df = pd.DataFrame({
    "drug":      ["Venetoclax", "Venetoclax", "Venetoclax"],
    "cell_line": ["HL60", "MOLT4", "K562"],
    "tcga_desc": ["LAML", "LAML", "CML"],
    "ln_ic50":   [-0.234, 0.567, 0.8]
})
df["IC50_uM"] = np.exp(df["ln_ic50"])
print(df.shape)
print(df.head())

#2. 
ds=pd.read_csv("Stage3/GDSC2-dataset.csv")
print(ds.shape,ds.columns.tolist(),ds.head(3))

#3
ds_venet = ds[ds["DRUG_NAME"] == "Venetoclax"].copy()
ds_sensitive = ds_venet[ds_venet["LN_IC50"] < 0]
print(len(ds_sensitive))

#4
ds_bcl2=ds[ds["PATHWAY_NAME"].str.contains("BCL-2",na=False)]
print(ds_bcl2["DRUG_NAME"].value_counts())

#5
ds_leu=ds[ds["TCGA_DESC"].isin(["LAML","ALL","CLL"])].copy()
print(len(ds_leu))

ds_venet["IC50_uM"]=np.exp(ds["LN_IC50"])
#6.
group=ds_venet.groupby("TCGA_DESC")["IC50_uM"].agg(["mean","count"]).reset_index()
top3=group.sort_values("mean").head(3)
print(top3)