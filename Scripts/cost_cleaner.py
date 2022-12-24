import pandas as pd
from clean_serials_tools import Cleaner

class FindCost():


    # Import csv (only specific columns)
    cost_csv_raw = pd.read_csv('assets/DT_export(baseline_model_cost).csv', usecols=['Model SKU', 'Current Base Line Cost'])

    # Find highest price
    # Later Addition: we now know the two highest are outliers. Adjusting trim range below to accomodate.
    print("FindCost test 1/4 : cost_csv_raw max")
    print(cost_csv_raw.max())

    # Trim to range
    cost_adjusted_range = cost_csv_raw[cost_csv_raw['Current Base Line Cost'].between(1, 301)]
    print("FindCost test 2/4 : cost_adjusted_range")
    print(cost_adjusted_range)

    # Sort by price high to low
    cost_sorted = cost_adjusted_range.sort_values(by='Current Base Line Cost', ascending=False)
    print("FindCost test 3/4 : cost_sorted")
    print(cost_sorted)

    # Remove intel processor denominations after I3/I5/I7 (i.e. I3DC, I5QC, I7HC)
    # These are not recorded upon receiving causing merge mismatch between dataframes
    cleaner_column = []

    for mod in cost_sorted['Model SKU']:
        cleaner_column.append(Cleaner.simple_i(mod))
    cost_sorted['MODEL'] = cleaner_column
    print("FindCost test 4/4 : cost_sorted")
    print(cost_sorted)

    # Save to new csv for inspection
    cost_sorted.to_csv('assets/cost_clean.csv')