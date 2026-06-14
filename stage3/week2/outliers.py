import pandas as pd
import numpy as np

df=pd.read_csv("Stage3/GDSC2-dataset.csv")
df_venet=df[df["DRUG_NAME"]=="Venetoclax"].copy()
df_venet["IC50_uM"]=np.exp(df_venet["LN_IC50"])

#2. flag outliers
df_venet["outlier"]=df_venet["Z_SCORE"].apply(lambda z: True if abs(z)>3 else False)

print("Outliers flagged:",df_venet["outlier"].sum())
print(df_venet[df_venet["outlier"]==True][["CELL_LINE_NAME","LN_IC50","Z_SCORE"]])

#3. remove outlier
df_clean=df_venet[df_venet["outlier"]==False].copy()
print(f"Before: {len(df_venet)} After:{len(df_clean)}")
print(f"Mean IC50 before: {df_venet['IC50_uM'].mean():.3f}uM")
print(f"Mean IC50 after:  {df_clean['IC50_uM'].mean():.3f} µM")