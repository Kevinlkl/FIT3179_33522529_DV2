import pandas as pd

# Read the trade data
df = pd.read_csv('trade_mys.csv')

# List of indicator names to filter for
target_indicators = [
    'Exports of goods and services (annual % growth)',
    'Exports of goods and services (% of GDP)',
    'Imports of goods and services (annual % growth)',
    'Imports of goods and services (% of GDP)',
    'Agricultural raw materials exports (% of merchandise exports)',
    'Agricultural raw materials imports (% of merchandise imports)',
    'Food exports (% of merchandise exports)',
    'Food imports (% of merchandise imports)',
    'Fuel exports (% of merchandise exports)',
    'Fuel imports (% of merchandise imports)',
    'ICT goods exports (% of total goods exports)',
    'ICT goods imports (% total goods imports)',
    'Insurance and financial services (% of commercial service exports)',
    'Insurance and financial services (% of commercial service imports)',
    'Manufactures exports (% of merchandise exports)',
    'Manufactures imports (% of merchandise imports)',
    'Ores and metals exports (% of merchandise exports)',
    'Ores and metals imports (% of merchandise imports)'
]

# Filter the dataframe for only the target indicators
filtered_df = df[df['Indicator Name'].isin(target_indicators)]

# Select only the required columns: Year, Indicator Name, and Value
result_df = filtered_df[['Year', 'Indicator Name', 'Value']].copy()

# Remove rows with missing values
result_df = result_df.dropna()

# Sort by year and indicator name for better organization
result_df = result_df.sort_values(['Year', 'Indicator Name'])

# Save to new CSV file
result_df.to_csv('mys_trade_indicators_filtered.csv', index=False)

print(f"Filtered data saved to 'trade_indicators_filtered.csv'")
print(f"Original dataset: {len(df)} rows")
print(f"Filtered dataset: {len(result_df)} rows")
print(f"Available indicators in filtered data:")
for indicator in sorted(result_df['Indicator Name'].unique()):
    count = len(result_df[result_df['Indicator Name'] == indicator])
    print(f"  - {indicator}: {count} data points")

# Indicator lists
net_indicators = [
    'Exports of goods and services (annual % growth)',
    'Exports of goods and services (% of GDP)',
    'Imports of goods and services (annual % growth)',
    'Imports of goods and services (% of GDP)'
]
sector_exports = [
    'Agricultural raw materials exports (% of merchandise exports)',
    'Food exports (% of merchandise exports)',
    'Fuel exports (% of merchandise exports)',
    'ICT goods exports (% of total goods exports)',
    'Insurance and financial services (% of commercial service exports)',
    'Manufactures exports (% of merchandise exports)',
    'Ores and metals exports (% of merchandise exports)'
]
sector_imports = [
    'Agricultural raw materials imports (% of merchandise imports)',
    'Food imports (% of merchandise imports)',
    'Fuel imports (% of merchandise imports)',
    'ICT goods imports (% total goods imports)',
    'Insurance and financial services (% of commercial service imports)',
    'Manufactures imports (% of merchandise imports)',
    'Ores and metals imports (% of merchandise imports)'
]

# Net import vs export (for overall goods and services)
net_df = df[df['Indicator Name'].isin(net_indicators)][['Year', 'Indicator Name', 'Value']].copy()
net_df = net_df.dropna()
net_df.to_csv('net_import_export.csv', index=False)

# Import by sector
import_df = df[df['Indicator Name'].isin(sector_imports)][['Year', 'Indicator Name', 'Value']].copy()
import_df = import_df.dropna()
import_df['Sector'] = import_df['Indicator Name'].str.replace(' imports (% of merchandise imports)', '', regex=False)
import_df['Sector'] = import_df['Sector'].str.replace(' imports (% total goods imports)', '', regex=False)
import_df['Sector'] = import_df['Sector'].str.replace('Insurance and financial services (% of commercial service imports)', 'Insurance and financial services', regex=False)
import_df = import_df[['Year', 'Sector', 'Value']]
import_df.to_csv('import_by_sector.csv', index=False)

# Export by sector
export_df = df[df['Indicator Name'].isin(sector_exports)][['Year', 'Indicator Name', 'Value']].copy()
export_df = export_df.dropna()
export_df['Sector'] = export_df['Indicator Name'].str.replace(' exports (% of merchandise exports)', '', regex=False)
export_df['Sector'] = export_df['Sector'].str.replace(' exports (% of total goods exports)', '', regex=False)
export_df['Sector'] = export_df['Sector'].str.replace('Insurance and financial services (% of commercial service exports)', 'Insurance and financial services', regex=False)
export_df = export_df[['Year', 'Sector', 'Value']]
export_df.to_csv('export_by_sector.csv', index=False)

print('CSV files created: net_import_export.csv, import_by_sector.csv, export_by_sector.csv')