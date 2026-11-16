"""
SELF-ASSESSMENT

1.A boolean filter evaluates a condition for every row in a DataFrame, marks it truen or false, and keeps only the rows where that condition is True.

2. df["revenue"]  returns a 1dimensional pandas Series, while df[["revenue"]] returns a 2dimensional pandas  with one column. This matters when passing data when you want table-style formatting.

3.Once written, a pandas script can clean, filter, and analyze millions of rows in seconds and you can rerun the exact same workflow on updated data files instantly.
"""

import pandas as pd


print("--- EXERCISE 1 ---")
df = pd.read_csv('data/retail_sales.csv')
print("Head:\n", df.head())
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nDtypes:\n", df.dtypes)



print("\n--- EXERCISE 2 ---")
south = df[df['region'] == 'South']
print("South row count:", len(south))
print("South head:\n", south.head())



print("\n--- EXERCISE 3 ---")
top_5_revenue = df.sort_values('revenue', ascending=False).head(5)
print("Top 5 by revenue:\n", top_5_revenue)



print("\n--- EXERCISE 4 ---")
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print("Big South row count:", len(big_south))
print("Big South head:\n", big_south.head())


print("\n--- EXERCISE 5 ---")
df['per_unit'] = df['revenue'] / df['quantity']
print("Head with per_unit column:\n", df.head())
print("\nMean per-unit price:", df['per_unit'].mean())


print("\n--- EXERCISE 6 ---")
print("Unique regions:", df['region'].unique())
print("\nRegion value counts:\n", df['region'].value_counts())


print("\n--- EXERCISE 7 ---")
subset_df = df[['region', 'product', 'revenue']]
print("Subset shape:", subset_df.shape)


print("\n--- EXERCISE 8 ---")
df.to_csv('data/explored.csv', index=False)
print("Saved updated DataFrame to 'data/explored.csv'.")