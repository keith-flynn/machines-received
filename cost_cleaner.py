import pandas as pd

# Check data types of columns
print(pd.read_csv('assets/DT_export(baseline_model_cost).csv').dtypes)

# Import csv (specific columns)
cost_raw = pd.read_csv('assets/DT_export(baseline_model_cost).csv', usecols=['Model SKU', 'Current Base Line Cost'])
print(cost_raw)

# Find highest price
# Later Addition: we now know the two highest are outliers. Adjusting trim range below to accomodate.
print(cost_raw.max())

# Trim to range
cost_adjusted_range = cost_raw[cost_raw['Current Base Line Cost'].between(1, 301)]
print(cost_adjusted_range)

# Sort by price high to low
cost_sorted = cost_adjusted_range.sort_values(by='Current Base Line Cost', ascending=False)

# Save to new csv for inspection
cost_sorted.to_csv('assets/cost_clean.csv')