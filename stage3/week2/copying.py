import pandas as pd
import numpy as np

df=pd.read_csv("Stage3/GDSC2-dataset.csv")
df_venet=df[df["DRUG_NAME"]=="Venetoclax"].copy()

#adding new coloumns
df_venet["IC50_uM"]=np.exp(df_venet["LN_IC50"])
df_venet["Sensitivity"]=df_venet["LN_IC50"].apply(lambda x: "High" if x < -1 else "Medium" if x < 1 else "Low"
)

print(df_venet["Sensitivity"].value_counts())
print("
Original df unchanged:", len(df), "rows")