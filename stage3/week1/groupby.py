import pandas as pd


df=pd.read_csv("Stage3/sanger-dose-response.csv")
df_vent=df[df["DRUG_NAME"]=="VENETOCLAX"]

summary = df_vent.groupby("DATASET")["IC50_PUBLISHED"].agg(
    ["mean", "median", "std", "count"]
).reset_index()

summary.columns = ["tissue", "mean_ic50", "median_ic50", "std_ic50", "n_cell_lines"]
print(summary.sort_values("mean_ic50").head(5))