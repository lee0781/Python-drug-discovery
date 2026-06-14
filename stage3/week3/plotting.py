import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1. bar chart by cancer type
df=pd.read_csv("Stage3/GDSC2-dataset.csv")
df["IC50_uM"]=np.exp(df["LN_IC50"])
df_venet=df[df["DRUG_NAME"]=="Venetoclax"].copy()
df_clean=df_venet[df_venet["Z_SCORE"].abs()<=3].copy()
df_clean["TCGA_DESC"]=df_clean["TCGA_DESC"].fillna("UNCLASSIFIED")

cancer_summary=df_clean.groupby("TCGA_DESC")["IC50_uM"].mean().sort_values()
cancer_summary.plot.bar(color="steelblue",figsize=(12,5),title="Mean Venetoclax IC50 by Cancer Type(GDSC2)")
plt.ylabel("Mean IC50 (uM)")
plt.xlabel("Cacner Type (TCGA)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("Venetolax_by_cancer.png",dpi=150)
plt.show()

#2. histogram of IC50 distribution
df_clean["IC50_uM"].plot.hist(bins=40,color="darkorange",edgecolor="white",figsize=(9,5),title="Venetoclax IC50 Distribution-944 Cell Lines(GDSC2)")
plt.xlabel("IC50_uM")
plt.ylabel("Number of Cell Lines")
plt.tight_layout()
plt.savefig("venetoclax)_dist.png",dpi=150)
plt.show()