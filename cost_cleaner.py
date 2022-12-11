import pandas as pd
import re
import matplotlib.pyplot as plt

# Function to remove "REC-" leading model names
def rec_remover():
    for elem in models_scan:
        model = re.sub(r"REC-", "", elem)
        count = data.SKU.value_counts()[elem]
        models_list.append(model)
        counts_list.append(count)

# Function to trim i-series processors to two-letter format
def simple_i(SKU_raw):
    # Create a list from the input string
    # Each item formerly separated by '-'
    split_model = SKU_raw.split("-")
    # Check the third list item for intel i-series
    # If true: slice it to the first two characters
    if split_model[2].startswith('I'):
        split_model[2] = split_model[2][0:2]
    # Else: we good
    else:
        pass
    # Return strings in list as one string, joined by '-'
    return '-'.join(split_model)

# Check data types of columns
print(pd.read_csv('assets/DT_export(baseline_model_cost).csv').dtypes)

# Import csv (specific columns)
cost_csv_raw = pd.read_csv('assets/DT_export(baseline_model_cost).csv', usecols=['Model SKU', 'Current Base Line Cost'])
print(cost_csv_raw)

# Find highest price
# Later Addition: we now know the two highest are outliers. Adjusting trim range below to accomodate.
print(cost_csv_raw.max())

# Trim to range
cost_adjusted_range = cost_csv_raw[cost_csv_raw['Current Base Line Cost'].between(1, 301)]
print(cost_adjusted_range)

# Sort by price high to low
cost_sorted = cost_adjusted_range.sort_values(by='Current Base Line Cost', ascending=False)
print(cost_sorted)

# Much later addition: After working on main body of project, more cleaning needed
# Remove intel processor denominations after I3/I5/I7 (i.e. I3DC, I5QC, I7HC)
# These are not recorded upon receiving causing merge mismatch between dataframes
cleaner_column = []

for mod in cost_sorted['Model SKU']:
    cleaner_column.append(simple_i(mod))
cost_sorted['MODEL'] = cleaner_column
print(cost_sorted)

# Save to new csv for inspection
cost_sorted.to_csv('assets/cost_clean.csv')