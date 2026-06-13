import pandas as pd

df = pd.read_csv(
    "data/processed_feedback.csv"
)

print(df.columns.tolist())