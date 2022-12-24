import pandas as pd
import re
import matplotlib.pyplot as plt
from clean_serials_tools import Cleaner
#from visualizations import ChartTime

"""
# Check data types of columns
print("test 1 : csv dtypes")
print(pd.read_csv('assets/DT_export(baseline_model_cost).csv').dtypes)

# Import csv (specific columns)
cost_csv_raw = pd.read_csv('assets/DT_export(baseline_model_cost).csv', usecols=['Model SKU', 'Current Base Line Cost'])
print("test 2 : cost_csv_raw")
print(cost_csv_raw)

# Find highest price
# Later Addition: we now know the two highest are outliers. Adjusting trim range below to accomodate.
print("test 3 : cost_csv_raw max")
print(cost_csv_raw.max())

# Trim to range
cost_adjusted_range = cost_csv_raw[cost_csv_raw['Current Base Line Cost'].between(1, 301)]
print("test 4 : cost_adjusted_range")
print(cost_adjusted_range)

# Sort by price high to low
cost_sorted = cost_adjusted_range.sort_values(by='Current Base Line Cost', ascending=False)
print("test 5 : cost_sorted")
print(cost_sorted)

# Much later addition: After working on main body of project, more cleaning needed
# Remove intel processor denominations after I3/I5/I7 (i.e. I3DC, I5QC, I7HC)
# These are not recorded upon receiving causing merge mismatch between dataframes
cleaner_column = []

for mod in cost_sorted['Model SKU']:
    cleaner_column.append(Cleaner.simple_i(mod))
cost_sorted['MODEL'] = cleaner_column
print("test 6 : cost_sorted")
print(cost_sorted)

# Save to new csv for inspection
cost_sorted.to_csv('assets/cost_clean.csv')
"""

class POMassager():

    # Import and save the SERIAL, SKU columns from csv
    data = pd.read_csv('assets/DT_export.csv', usecols=['SERIAL', 'SKU'])

    # create a list of the unique models in receiving format
    models_scan = []
    for i in data.SKU:
        if i not in Cleaner.models_scan:
            Cleaner.models_scan.append(i)

    # iterate through models list removing receiving format
    # and add total count

    # There two columns are legacy
    #counts_list = []
    #models_list = []

    # Call function to remove "REC-" leading model names
    # Prints machine quantities to the terminal to be copied/pasted for a follow-up email to the boss
    Cleaner.rec_remover(data)

    # Pandas datafram from the counts/models lists
    df = pd.DataFrame(columns=['MODEL', 'COUNT'])
    df['MODEL'] = Cleaner.models_list
    df['COUNT'] = Cleaner.counts_list

    # Bring in cost data
    cost = pd.read_csv('assets/cost_clean.csv', usecols=['Model SKU', 'Current Base Line Cost', 'MODEL'])

    # Rename long-winded column name which has lowercase letters to better fit
    cost.rename(columns = {'Model SKU' : 'MODELS', 'Current Base Line Cost' : 'COST'}, inplace=True)
    print("test 1 : cost")
    print(cost)

    # df.join(cost)
    test_merge = pd.merge(df, cost)
    print("test 2 : test_merge")
    print(test_merge)

    # Group machines by AVERAGE price of model if multiple costs exist
    avg_merge = test_merge.groupby(['MODEL'], as_index=False).mean(numeric_only=True)

    # Now change float to int
    # Making these columns whole numbers
    avg_merge.COST = avg_merge.COST.astype(int)
    avg_merge.COUNT = avg_merge.COUNT.astype(int)
    print("test 3 : avg_merge")
    print(avg_merge)

    # 3070 mini i7 model doesn't have a base cost yet. 
    # It doesn't meet merge criteria and will be discarded when dataframes merge
    # Need to account for this with notification
    no_price = pd.merge(df, cost, how='left', indicator=False)

    # Check for any machines with a NaN value in no_price dataframe
    if no_price.COST.isnull().values.any():
        print("****************************************")
        print("*  Machines with no cost basis (NaN):  *")
        print("****************************************")
        print(no_price[no_price['COST'].isna()])
    else :
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~  All machines received have existing cost basis.  ~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # New cost of PO df to make a visualization with lambda fun
    cost_vis = avg_merge
    cost_vis['TOTAL'] = cost_vis.apply(lambda x: x['COUNT'] * x['COST'], axis=1)
    print("test 4 : cost_vis")
    print(cost_vis)
    total_cost = str(cost_vis['TOTAL'].sum())
    print("Estimated total PO cost: $" + total_cost)
    # Make a percentage column for cost_vis df. Each item in total column / total of whole column * 100 to play nice with charting
    #cost_vis['TOTALPCT'] = cost_vis.apply(lambda x: (x['TOTAL'] / POMassager.cost_vis['TOTAL'].sum()) * 100, axis=1)
    #print("test 5 : cost_vis again")
    #print(cost_vis)


"""
# visuals
plt.style.use('dark_background')
df_sorted = df.sort_values(by='COUNT', ascending=False)
plt.figure(figsize=(10,7), dpi=80)
plt.bar(df_sorted.MODEL, df_sorted.COUNT)
plt.xticks(rotation=45, fontsize=13)
plt.title('Machines Received', fontsize=20)
plt.ylabel('Number of Machines', fontsize=13)
plt.tight_layout()
plt.show()

sorted_cost_vis = cost_vis.sort_values(by='TOTALPCT', ascending=False)
labels = sorted_cost_vis['MODEL']
sizes = sorted_cost_vis['TOTALPCT']

# Explode second largest wedge:
# A loop to create a tuple that serves as the (pie chart wedge) explode function data
# I realize an exploded wedge is meant to emphasize something,
# but I simply like how it looks like pac-man every time and I wanted to make this feature scalable across datasets
myexplode = ()
for i in sorted_cost_vis['TOTALPCT']:
    if len(myexplode) == 1:
        myexplode = myexplode + (0.2,)
    else:
        myexplode = myexplode + (0,)

fig1, ax1, = plt.subplots(figsize=(10,7), dpi=80)

# I don't really understand the _, but it's needed to change the autotext color
_, _, autotexts = ax1.pie(sizes, labels = labels, explode = myexplode, shadow=True, autopct='%1.1f%%', startangle=45)
# Make inner text more readable
for autotext in autotexts:
    autotext.set_color('black')

plt.suptitle('PO Cost Allocation', fontsize=20)
plt.title('Estimated Price: $' + total_cost)
ax1.axis('equal')
plt.show()
"""