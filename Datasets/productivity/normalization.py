import pandas as pd

# Read the CSV file
df = pd.read_csv('productivity_annual.csv')

# Convert date to datetime and extract year
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

# Filter for only the sectors we want and series 'abs'
df_filtered = df[(df['sector'].isin(['p1', 'p2', 'p3', 'p4', 'p5'])) & 
                 (df['series'] == 'abs')].copy()

# Get base year values (2015) for each sector
base_values = df_filtered[df_filtered['year'] == 2015].groupby('sector')['output_hour'].mean()

print("Base year (2015) values:")
print(base_values)

# Create normalized values
def normalize_to_base_year(row):
    sector = row['sector']
    base_value = base_values.get(sector)
    if base_value and pd.notna(base_value) and base_value != 0:
        return (row['output_hour'] / base_value) * 100
    else:
        return None

df_filtered['normalized_productivity'] = df_filtered.apply(normalize_to_base_year, axis=1)

# Display sample results
print("\nSample of normalized data:")
print(df_filtered[['year', 'sector', 'output_hour', 'normalized_productivity']].head(10))

# Save the normalized data
df_filtered.to_csv('productivity_annual_normalized.csv', index=False)

print("\nNormalized data saved to 'productivity_annual_normalized.csv'")

# Show summary statistics
print("\nSummary by sector:")
summary = df_filtered.groupby('sector').agg({
    'output_hour': ['min', 'max', 'mean'],
    'normalized_productivity': ['min', 'max', 'mean']
}).round(2)
print(summary)