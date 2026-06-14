import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1. 
df=pd.read_csv("Stage3/GDSC2-dataset.csv")
#2.
print("DataFrame shape:",df.shape)
unknown=df.isna()
print("Missing Values:",unknown.sum())
#3.
df["TCGA_DESC"]=df["TCGA_DESC"].fillna("NAN")
df["PUTATIVE_TARGET"]=df["PUTATIVE_TARGET"].fillna("NAN")
#4.
df["IC50_uM"]=np.exp(df["LN_IC50"])
#5.
df_mirin=df[df["DRUG_NAME"]=="Mirin"].copy()
#6.
df_mirin["sensitivity"]=df_mirin["LN_IC50"].apply(lambda x: "High" if x<-1 else "Medium" if x<1 else "Low")
#7.
df_mirin["outliers"]=df_mirin["Z_SCORE"].apply(lambda z:True if abs(z)>3 else False)
print("Outliers flagged:", df_mirin["outliers"].sum())
clean=df_mirin[df_mirin["outliers"]==False].copy()
print(f"Before: {df_mirin.shape} After: {clean.shape}")
#8.
group=clean.groupby("TCGA_DESC")["IC50_uM"].agg(["mean","count"])
#9.
top5=clean.nsmallest(5,"LN_IC50")
print("top5 sensitve cell lines:",top5[["CELL_LINE_NAME", "TCGA_DESC", "IC50_uM"]].round(4))
#10.
for i, (index,row) in enumerate (top5.iterrows(),start=1):
    name=row["CELL_LINE_NAME"]
    cancer=row["TCGA_DESC"]
    ic50=row["IC50_uM"]
    label="Ultra" if ic50<0.1 else "sensitive"
    print(f"{i:>2}. {name:<20} {cancer:<15} IC50={ic50:.4f} µM  {label}")
    
#11.
# Step 1 — group
summary = clean.groupby("TCGA_DESC")["IC50_uM"].mean().sort_values()

# Step 2 — bar chart
summary.plot.bar(figsize=(12, 5), color="steelblue", edgecolor="white")

# Step 3 — labels
plt.xlabel("Cancer Type")
plt.ylabel("Mean IC50 (µM)")
plt.title("Mirin Mean IC50 by Cancer Type (GDSC2)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("mirin_by_cancer.png", dpi=150)
plt.show()
#12.
clean.to_csv("Stage3/mirin_clean.csv", index=False)
print("Saved")