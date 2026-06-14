# GDSC2 Venetoclax Sensitivity Analysis
# Data: Genomics of Drug Sensitivity in Cancer (Sanger Institute)
# Author: Youngwon Lee

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Stage3/GDSC2-dataset.csv")
print("="*50)
print("GDSC2 Dataset Overview")
print("="*50)
print("\nDataFrame Shape:",df.shape)
print("\nDataFrame Columns:\n",df.columns.tolist())
print("\nMissing Values:\n",df.isna().sum())

df["TCGA_DESC"]=df["TCGA_DESC"].fillna("UNIDENTIFIED")
df["PUTATIVE_TARGET"]=df["PUTATIVE_TARGET"].fillna("UNIDENTIFIED")
print("\nMissing values after cleaning:")
print(f"TCGA_DESC:{df['TCGA_DESC'].isna().sum()}")
print(f"PUTATIVE_TARGET:{df['PUTATIVE_TARGET'].isna().sum()}")

df["IC50_uM"]=np.exp(df["LN_IC50"])

df_venet=df[df["DRUG_NAME"]=="Venetoclax"].copy()
print(f"Venetoclax experiments: {len(df_venet)}")

df_venet["sensitivity"]=df_venet["LN_IC50"].apply(lambda x: "High" if x<-1 else "Medium" if x<1 else "Low")
print("\nSensitivity breakdown:")
print(df_venet["sensitivity"].value_counts())

df_venet["outlier"]=df_venet["Z_SCORE"].apply(lambda z: True if abs(z)>3 else False)
print(f"\nOutliers flagged: {df_venet['outlier'].sum()}")
df_clean=df_venet[df_venet["outlier"]==False].copy()
print(f"Before:{df_venet.shape} After: {df_clean.shape}")

summary=df_clean.groupby("TCGA_DESC")["IC50_uM"].agg(["mean","count"]).reset_index()
summary=summary.sort_values("mean")
print("\nMean IC50 by cancer type (most sensitive first)")
print(summary.head(10).round(3))

top10=df_clean.nsmallest(10,"IC50_uM")
print("\nTop10 most sensitive cell lines:")
print(top10[["CELL_LINE_NAME","TCGA_DESC","IC50_uM"]].round(4))

print("\n Top 10 Most Sensitive Cell Lines (Venetoclax)")
for i, (index,row) in enumerate(top10.iterrows(),start=1):
    name= row["CELL_LINE_NAME"]
    cancer=row["TCGA_DESC"]
    ic50=row["IC50_uM"]
    label="ULTRA" if ic50<0.1 else "SENSITIVE"
    print(f"{i:>2}. {name:<20} {cancer:<15} IC50={ic50:.4f} µM  {label}")

plot_data = summary.set_index("TCGA_DESC")["mean"]
plot_data.plot.bar(color="steelblue", figsize=(12, 5), title="Mean Venetoclax IC50 by Cancer Type")
plt.ylabel("Mean IC50 (µM)")
plt.xlabel("Cancer Type (TCGA)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("venetoclax_by_cancer.png", dpi=150)
plt.show()

print("\nHistogram")
df_clean["IC50_uM"].plot.hist(bins=40, color="darkorange",edgecolor="white", figsize=(9,5),title=f"Venetoclax IC50 Distribution — {len(df_clean)} Cell Lines (GDSC2)")
plt.xlabel("IC50 (µM)")
plt.ylabel("Number of Cell Lines")
plt.tight_layout()
plt.savefig("venetoclax_dist.png", dpi=150)
plt.show()

df_clean.to_csv("Stage3/venetoclax_clean.csv", index=False)
print("\n Cleaned data saved to venetoclax_clean.csv")

git pull --rebase origin main
git add stage3/
git commit -m "[Stage 3] Venetoclax GDSC2 analysis — IC50, sensitivity, outlier removal, cancer type comparison"
git push origin main