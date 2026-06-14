import pandas as pd
import numpy as np

df=pd.read_csv("Stage3/GDSC2-dataset.csv")
df_venet=df[df["DRUG_NAME"]=="Venetoclax"].copy()
df_venet["IC50_uM"]=np.exp(df_venet["LN_IC50"])
df["sensitivity"]=