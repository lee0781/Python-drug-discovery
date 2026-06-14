import pandas as pd
import numpy as np
print("pandas version:", pd.__version__)

df=pd.DataFrame({"drug_name": ["Venetoclax","Venetoclax","Venetoclax"],
                 "cell_line": ["HL60","MOLT-4","Jurkat"],
                 "ic50_um": [2.53,34.50,1.24],
                 "r2": [0.9999,0.9996,0.9997],
                 "response": ["Sensitive","Resistant","Sensitive"],})
print(df)

print("Shape:",df.shape)
print("Columns:",df.columns.tolist())
print("types:",df.dtypes)
print("first 2 rows:",df.head(2))
print(f"Mean IC50: {df['ic50_um'].mean():.3f}")