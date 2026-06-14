import pandas as pd
import numpy as np

#1. 
df=pd.read_csv("Stage3/GDSC2-dataset.csv")

#2.
df.info()
print("Shape:",df.shape)
print("Missing values:",df.isna().sum())

#3.
df["TCGA_DESC"]=df["TCGA_DESC"].fillna("UNK")
df["PUTATIVE_TARGET"]=df["PUTATIVE_TARGET"].fillna("UNK")

#4. 
df["IC50_uM"]=np.exp(df["LN_IC50"])

#5.
df_venet=df[df["DRUG_NAME"]=="Venetoclax"].copy()

#6.
df_venet["sensitivity"]=df_venet["LN_IC50"].apply(lambda x: "high" if x<-1 else "medium" if x<1 else "low")

#7.
df_venet["outlier"]=df_venet["Z_SCORE"].apply(lambda z: True if abs(z)>3 else False)
print("Outliers flagged:",df_venet["outlier"].sum())

#8.
df_venet_clean=df_venet[df_venet["outlier"]==False].copy()
print(f"Before: {len(df_venet)} After: {len(df_venet_clean)}")

#9. need more practice
summary=df_venet_clean.groupby("TCGA_DESC")["IC50_uM"].agg(["mean","count"]).reset_index()
print(summary.sort_values("mean").head(5))

#10
df_venet_clean.to_csv("Stage3/venetoclax_clean.csv",index=False)

#11.
print("======Summary Report=====")
print(f"Total Venetoclax experiments:{len(df_venet)}")
print(f"Outlier removed:{df_venet['outlier'].sum()}")
print(f"Clean experiments: {len(df_venet_clean)}")
print(f"Mean IC50: {df_venet_clean['IC50_uM'].mean():.3f}uM")
print(f"Senitivity breakdown:")
print(df_venet['sensitivity'].value_counts())
print(f"Top 3 most sensitive cancer types:")
print(summary.sort_values("mean").head(3))

