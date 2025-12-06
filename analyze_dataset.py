import pandas as pd

# Read the dataset
df = pd.read_csv('dataset/Articles.csv', encoding='latin-1')

print("=" * 60)
print("DATASET SUMMARY")
print("=" * 60)
print(f"\nDataset shape: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"\nColumns: {list(df.columns)}")
print(f"\nData types:")
print(df.dtypes)
print(f"\nFirst few rows (non-Article columns):")
print(df[['Date', 'Heading', 'NewsType']].head(5))
print(f"\nNewsType distribution:")
print(df['NewsType'].value_counts())
print(f"\nDate range:")
print(f"  Earliest: {df['Date'].min()}")
print(f"  Latest: {df['Date'].max()}")
print(f"\nSample article text (first 200 chars):")
if len(df['Article'].iloc[0]) > 0:
    print(df['Article'].iloc[0][:200] + "...")
print(f"\nMissing values:")
print(df.isnull().sum())

