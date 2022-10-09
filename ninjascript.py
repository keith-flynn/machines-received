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
        print(model, count)

# import and save the SERIAL, SKU columns from csv
data = pd.read_csv('assets/DT_export.csv', usecols=['SERIAL', 'SKU'])

# create a list of the unique models in receiving format
models_scan = []
for i in data.SKU:
    if i not in models_scan:
        models_scan.append(i)

# iterate through models list removing receiving format
# and add total count
counts_list = []
models_list = []

# Call function to remove "REC-" leading model names
# Prints machine quantities to the terminal to be copied/pasted for a follow-up email to the boss
rec_remover()

# Pandas datafram from the counts/models lists
df = pd.DataFrame(columns=['MODELS', 'COUNT'])
df['MODELS'] = models_list
df['COUNT'] = counts_list

# Bring in cost data
cost = pd.read_csv('assets/cost_clean.csv', usecols=['Model SKU', 'Current Base Line Cost'])
cost.rename(columns = {'Model SKU' : 'MODELS', 'Current Base Line Cost' : 'COST'}, inplace=True)
print(cost)

#df.join(cost)
test_merge = pd.merge(df, cost)
print(test_merge)

# Group machines by AVERAGE price of model if multiple costs exist
avg_merge = test_merge.groupby(['MODELS'], as_index=False).mean()
#avg_merge = test_merge.groupby(['MODELS', 'COUNT']).agg([np.average])
# Now change float to int

# Making these columns whole numbers
avg_merge.COST = avg_merge.COST.astype(int)
avg_merge.COUNT = avg_merge.COUNT.astype(int)
print(avg_merge)

# 3070 doesn't have a base cost yet. 
# It doesn't meet merge criteria and will be discarded when dataframes merge
# Need to account for this with notification
no_price = pd.merge(df, cost, how='left', indicator=False)

print("**********************************")
print("*  Machines with no cost basis:  *")
print("**********************************")
print(no_price[no_price['COST'].isna()])

# New cost of PO df to make a visualization with lambda fun
cost_vis = avg_merge
cost_vis['TOTAL'] = cost_vis.apply(lambda x: x['COUNT'] * x['COST'], axis=1)
print(cost_vis)
total_cost = str(cost_vis['TOTAL'].sum())
print("Estimated total PO cost: $" + total_cost)
# Make a percentage column for cost_vis df. Each item in total column / total of whole column * 100 to play nice with charting
cost_vis['TOTALPCT'] = cost_vis.apply(lambda x: (x['TOTAL'] / cost_vis['TOTAL'].sum()) * 100, axis=1)
print(cost_vis)
# Making sure these percentages add up to 100
print(cost_vis['TOTALPCT'].sum())

# visuals
plt.style.use('dark_background')
df_sorted = df.sort_values(by='COUNT', ascending=False)
plt.bar(df_sorted.MODELS, df_sorted.COUNT)
plt.xticks(rotation=45, fontsize=7)
plt.title('Machines Received')
plt.tight_layout()
plt.show()

sorted_cost_vis = cost_vis.sort_values(by='TOTALPCT', ascending=False)
labels = sorted_cost_vis['MODELS']
sizes = sorted_cost_vis['TOTALPCT']

# Explode second largest wedge:
# A loop to create a tuple that serves as the (pie chart wedge) explode function data
# I realize an exploded wedge is meant to emphasize something,
# but I simply like how it looks like pac-man every time and I wanted to make this feature scalable across datasets
myexplode = ()
for i in sorted_cost_vis['TOTALPCT']:
    print(i)
    if len(myexplode) == 1:
        myexplode = myexplode + (0.2,)
    else:
        myexplode = myexplode + (0,)
    print(myexplode)

fig1, ax1, = plt.subplots()
# I don't really understand the _, but it's needed to change the autotext color
_, _, autotexts = ax1.pie(sizes, labels = labels, explode = myexplode, shadow=True, autopct='%1.1f%%', startangle=45)
# Make inner text more readable
for autotext in autotexts:
    autotext.set_color('black')

plt.suptitle('PO Cost Allocation')
plt.title('Estimated Price: $' + total_cost)
ax1.axis('equal')
plt.show()
