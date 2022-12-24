import pandas as pd
import re
import matplotlib.pyplot as plt
from clean_serials_tools import Cleaner

class POMassager():

    # Import and save the SERIAL, SKU columns from csv
    data = pd.read_csv('assets/DT_export.csv', usecols=['SERIAL', 'SKU'])

    # create a list of the unique models in receiving format
    models_scan = []
    for i in data.SKU:
        if i not in Cleaner.models_scan:
            Cleaner.models_scan.append(i)

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
    print("POMassager test 1/4 : cost")
    print(cost)

    # df.join(cost)
    test_merge = pd.merge(df, cost)
    print("POMassager test 2/4 : test_merge")
    print(test_merge)

    # Group machines by AVERAGE price of model if multiple costs exist
    avg_merge = test_merge.groupby(['MODEL'], as_index=False).mean(numeric_only=True)

    # Now change float to int
    # Making these columns whole numbers
    avg_merge.COST = avg_merge.COST.astype(int)
    avg_merge.COUNT = avg_merge.COUNT.astype(int)
    print("POMassager test 3/4 : avg_merge")
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
    print("POMassager test 4/4 : cost_vis")
    print(cost_vis)
    total_cost = str(cost_vis['TOTAL'].sum())
    print("Estimated total PO cost: $" + total_cost)
