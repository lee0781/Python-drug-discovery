import pandas as pd
import numpy as np

df=pd.read_csv("Stage3/GDSC2-dataset.csv")
df["IC50_uM"]=np.exp(df["LN_IC50"])

#create a drug info table 
drug_info=df[["DRUG_NAME","PUTATIVE_TARGET","PATHWAY_NAME"]].drop_duplicates()
drug_info=drug_info[drug_info["PUTATIVE_TARGET"].notna()]

#get venetoclax sensitivity
venet_summary=df[df["DRUG_NAME"]=="Venetoclax"].copy()
venet_summary=venet_summary[["DRUG_NAME","CELL_LINE_NAME","TCGA_DESC","IC50_uM"]]

#merge
df_merged=pd.merge(venet_summary,drug_info,on="DRUG_NAME",how="inner")

print("Merged shape:", df_merged.shape)
print(df_merged.head(1))