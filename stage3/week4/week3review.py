import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1. 
df = pd.read_csv("Stage3/GDSC2-dataset.csv")
df_venet = df[df["DRUG_NAME"] == "Venetoclax"].copy()
df_venet["IC50_uM"] = np.exp(df_venet["LN_IC50"])
top5 = df_venet.sort_values("LN_IC50").head(5)
print(top5[["CELL_LINE_NAME", "TCGA_DESC", "IC50_uM"]].round(4))

#2.
sensitive = df_venet.nsmallest(5, "LN_IC50")
resistant = df_venet.nlargest(5, "LN_IC50")

print("Top 5 Sensitive:")
print(sensitive[["CELL_LINE_NAME", "TCGA_DESC", "IC50_uM"]].round(4))
print("\nTop 5 Resistant:")
print(resistant[["CELL_LINE_NAME", "TCGA_DESC", "IC50_uM"]].round(4))

#3.
for i, (index,row) in enumerate(top5.iterrows(),start=1):
    name     = row["CELL_LINE_NAME"]
    cancer   = row["TCGA_DESC"]
    ic50     = row["IC50_uM"]
    pathway  = row["PATHWAY_NAME"]
    label = "⭐ ULTRA" if ic50 < 0.1 else "✅ Sensitive"
    print(f"{i:>2}. {name:<20} {cancer:<8} IC50={ic50:.4f} µM  {pathway:<25} {label}")

#4. 
my_drugs = pd.DataFrame({
    "DRUG_NAME": ["Venetoclax", "Gefitinib", "Osimertinib", "Navitoclax", "Imatinib"],
    "phase":     ["Phase 3", "Phase 2", "Phase 3", "Phase 1", "Approved"]
})

merged = pd.merge(my_drugs, df, on="DRUG_NAME", how="left")
print(merged.shape)

#5.
# Step 1 — group
summary = df_venet.groupby("TCGA_DESC")["IC50_uM"].mean().sort_values()

# Step 2 — bar chart
summary.plot.bar(figsize=(12, 5), color="steelblue", edgecolor="white")

# Step 3 — labels
plt.xlabel("Cancer Type")
plt.ylabel("Mean IC50 (µM)")
plt.title("Venetoclax Mean IC50 by Cancer Type (GDSC2)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("venetoclax_by_cancer.png", dpi=150)
plt.show()