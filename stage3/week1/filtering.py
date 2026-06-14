import pandas as pd
import numpy as np
df=pd.read_csv("Stage3/sanger-dose-response.csv")
df_venet=df[df["DRUG_NAME"]=="VENETOCLAX"]
print("Venetoclax rows:",len(df_venet))

df_sensitive=df[df["IC50_PUBLISHED"]<1.0]
print("Highly sensitive screens:", len(df_sensitive))

#2. .isin
bcl2_drugs=["VENETOCLAX","NAVITOCLAX"]
df_bcl2=df[df["DRUG_NAME"].isin(bcl2_drugs)]
print(df_bcl2["DRUG_NAME"].value_counts())

#3.
df_hits=df[(df["DRUG_NAME"]=="VENETOCLAX")&(df["IC50_PUBLISHED"]<1.0)]
print("Venetoclax hits:", len(df_hits))



df_gdsc2 = df[df["DATASET"] == "GDSC2"]
print("GDSC2 rows:", len(df_gdsc2))