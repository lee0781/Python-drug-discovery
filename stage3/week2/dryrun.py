import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#2
df=pd.read_csv("Stage3/GDSC2-dataset.csv")

#3
print(df.shape,
      df.columns.tolist(),
      df.head(),
      df.info())

#4
df["TCGA_DESC"]=df["TCGA_DESC"].fillna("UNCLASSIFIED")

#5.
df["PUTATIVE_TARGET"]=df["PUTATIVE_TARGET"].fillna("UNKNOWN")

#6
df["IC50_uM"]=np.exp(df["LN_IC50"])

#7
df_venet=df[df["DRUG_NAME"]=="Venetoclax"].copy()

#8
df_venet["sensitivity"]=df_venet["LN_IC50"].apply(lambda x: "High" if x<-1 else "Medium" if x<1 else "Low" )

#9
df_venet["outlier"]=df_venet["Z_SCORE"].apply(lambda z: True if abs(z)>3 else False)
print("outliers flagged:",df_venet["outlier"].sum())

#10
df_venet_clean=df_venet[df_venet["outlier"]==False].copy()
print(f"Before:{len(df_venet)} After: {len(df_venet_clean)}")

#11
summary=df_venet_clean.groupby("TCGA_DESC")["IC50_uM"].agg(["mean","count"])

#12
top5=df_venet_clean.groupby("TCGA_DESC")["IC50_uM"].mean().reset_index()
top5=top5.sort_values("IC50_uM").head(5)
print(top5)