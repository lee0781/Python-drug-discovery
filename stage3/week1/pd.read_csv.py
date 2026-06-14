import pandas as pd
import numpy as np

df=pd.read_csv("Stage3/sanger-dose-response.csv")
print('loaded shape:',df.shape)

print(df.info())
print(df.head())

print(df.describe())
print(df["DRUG_NAME"].value_counts().head(10))

print("Venetoclax in data:","Venetoclax" in df["DRUG_NAME"].values)
venetoclax_rows=df[df["DRUG_NAME"]=="Venetoclax"]
print("Venetoclax screens:", len(venetoclax_rows))