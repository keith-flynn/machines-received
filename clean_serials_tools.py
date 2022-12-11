import re

class Cleaner():

    def __init__(self):
        pass

    counts_list = []
    models_list = []
    models_scan = []

    # Function to remove "REC-" leading model names
    def rec_remover(df):
        for elem in Cleaner.models_scan:
            model = re.sub(r"REC-", "", elem)
            count = df.SKU.value_counts()[elem]
            Cleaner.models_list.append(model)
            Cleaner.counts_list.append(count)

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

    # create a list of the unique models in receiving format
    """
    for i in data.SKU:
        if i not in models_scan:
            models_scan.append(i)

"""