import pandas as pd
import re
import matplotlib.pyplot as plt

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

for elem in models_scan:
    model = re.sub(r"REC-", "", elem)
    count = data.SKU.value_counts()[elem]
    models_list.append(model)
    counts_list.append(count)
    print(model, count)

# Pandas datafram from the counts/models lists
df = pd.DataFrame(columns=['MODELS', 'COUNT'])
df['MODELS'] = models_list
df['COUNT'] = counts_list

# visuals
plt.style.use('dark_background')
df_sorted = df.sort_values(by='COUNT', ascending=False)
plt.bar(df_sorted.MODELS, df_sorted.COUNT)
plt.xticks(rotation=45, fontsize=7)
plt.title('Machines Received')
plt.tight_layout()
plt.show()