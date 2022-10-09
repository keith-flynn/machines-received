import pandas as pd
import numpy as np
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
#df.append(cost.duplicated().iloc[df.shape[0]:], ignore_index=True)
avg_merge = test_merge.groupby(['MODELS', 'COUNT']).agg([np.average])
# Now change float to int
avg_merge.COST = avg_merge.COST.astype(int)
print(avg_merge)

# 3070 doesn't have a base cost yet. Need to account for this with notification
no_price = pd.merge(df, cost, how='left', indicator=False)
#no_price = df[~df['MODELS'].isin(avg_merge.MODELS)]
#no_price = pd.concat([df['MODELS'], avg_merge['MODELS']]).drop_duplicates(keep=False)

print("**********************************")
print("*  Machines with no cost basis:  *")
print("**********************************")
print(no_price[no_price['COST'].isna()])

# visuals
plt.style.use('dark_background')
df_sorted = df.sort_values(by='COUNT', ascending=False)
plt.bar(df_sorted.MODELS, df_sorted.COUNT)
plt.xticks(rotation=45, fontsize=7)
plt.title('Machines Received')
plt.tight_layout()
plt.show()