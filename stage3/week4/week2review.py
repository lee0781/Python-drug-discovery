import numpy as np
import pandas as pd

#1.
df=pd.read_csv("Stage3/GDSC2-dataset.csv")
print((df["TCGA_DESC"].isna().sum()))

df["TCGA_DESC"]=df["TCGA_DESC"].fillna("UNCLASSIFIED")
df["PUTATIVE_TARGET"]=df["PUTATIVE_TARGET"].fillna("Unknown")
print(df["TCGA_DESC"].isna().sum())
print(df["PUTATIVE_TARGET"].isna().sum())


#2. 
df_venet=df[df["DRUG_NAME"]=="Venetoclax"].copy()
# copy() is required to not intervene the main data fram with changes

#3.
df_venet["sensitivity"]=df_venet["LN_IC50"].apply(lambda x: "High" if x<-1 else "Medium" if x<1 else "Low")
print(df_venet["sensitivity"].value_counts())

#4.
df_venet["outliers"] = df_venet["Z_SCORE"].apply(lambda z: True if abs(z) > 3 else False)
print("Outliers flagged:", df_venet["outliers"].sum())

df_clean = df_venet[df_venet["outliers"] == False].copy()
print(f"Before: {df_venet.shape} After: {df_clean.shape}")

#5
before=np.exp(df_venet["LN_IC50"]).mean()
after=np.exp(df_clean["LN_IC50"]).mean()

print("before:",before)
print("after mean:",after)
