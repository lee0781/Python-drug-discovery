import pandas as pd

#1
df=pd.read_csv("Stage3/sanger-dose-response.csv")

#2
print("data shape:",df.shape)
print("data columns:",df.columns.tolist())
print(df.head())

#3.
df_venet=df[df["DRUG_NAME"]==("VENETOCLAX")]
print("\nVenetolax rows:",len(df_venet))
#4. 
summary=df_venet.groupby("DATASET")["IC50_PUBLISHED"].agg(["mean","count"]).reset_index()
print("\n── IC50 by Dataset ──")
print(summary)

#5.
df_sensitive=df_venet[df_venet["IC50_PUBLISHED"]<1.0]
print("\n── Highly Sensitive Screens (IC50 < 1 µM) ──")
print("count:",len(df_sensitive))
print(df_sensitive[["ARXSPAN_ID", "IC50_PUBLISHED", "DATASET"]].head(5))

#6
df_gdsc2_venet=df_venet[df_venet["DATASET"]=="GDSC2"]
print("\n── GDSC2 Venetoclax Only ──")
print("GDSC2 screens:", len(df_gdsc2_venet))

#7. Clean summary report
print("\n── Summary Report ──")
print(f"Drug: VENETOCLAX")
print(f"Total screens: {len(df_venet)}")
print(f"Mean IC50: {df_venet['IC50_PUBLISHED'].mean():.3f} µM")
print(f"Highly sensitive (IC50 < 1 µM): {len(df_sensitive)}")
print(f"GDSC2 screens: {len(df_gdsc2_venet)}")