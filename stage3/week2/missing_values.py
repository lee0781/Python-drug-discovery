import pandas as pd
import numpy as np

df=pd.read_csv("Stage3/GDSC2-dataset.csv")

#1. find missing values
print("Missing values per column")
print(df.isna().sum())
print("Percentage missing:")
print((df.isna().sum()/len(df)*100).round(2))

#2. fill missing TCGA-DESC with "unclassified"
df["TCGA_DESC"]=df["TCGA_DESC"].fillna("UNCLASSIFIED")
print("TCGA_DESC after fillna:",df["TCGA_DESC"].isna().sum(),"NaN remaining")

#3. fill missing putative target
df["PUTATIVE_TARGET"]=df["PUTATIVE_TARGET"].fillna("Unknown")

#4. 
print("Remaining NAN aftera cleaning:")
print(df[["TCGA_DESC","PUTATIVE_TARGET"]].isna().sum())