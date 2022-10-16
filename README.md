# Machines Received

## Automate purchase order data visualizations
---
## Project Overview:
- Imports raw price data and cleans
- Imports purchase order data and cleans
- Produces useful information about purchase orders
- Generates two visualizations:
  - Bar graph of machine types received by total units
  - Pie chart of which models account for total cost
---
##### **Required packages**
##### - _Pandas_
##### - _Matplotlib_
##### - from the command prompt, input `pip install pandas` and `pip install matplotlib` to add required modules
---
### **The basics:**
A jupyter notebook that takes data from a purchase order and processes it to display relevant information. This code is not specific to one CSV, but is scalable to all CSV files generated in this format. An export tool within my workplace's website generates these CSVs with consistent formatting, and column titles are the main data manipulation methodology used.
---
---
### *Project features:*
1. Read in data from a local csv
2. Use built-in python, pandas, functions/lambdas to manipulate data
3. Analyze with built-in python/pandas and custum functions
4. Make basic plots with matplotlib
5. Markdown cells in Jupyter Notebook explaining throught process and code
---
### **In detail:**
 A cost basis CSV is first cleaned to be universally applicable to machines in their receiving format. Data from a received purchase order is then imported, cleaned, and made into a dataframe visualizing its makeup by number of machines. Cost values from the cost basis CSV are then merged to create a visualization for estimated total price and breakdown by model. The machines are then totaled by value using the average price, and a second visualization displays the projected average cost, along with a percentage representation of each model received.
---
#### Sample Visualizations:
![sample-bar](../assets/sample-bar.png?raw=true)
---
##### This final project for Code Kentucky Data Analysis I is a continuation of my functional work program [ninjascripts](https://github.com/keith-flynn/ninjascripts/). My latest edition includes a file browser GUI to select which .csv file to import, and a section which automatically copies all of the serial numbers to the [system agnostic] operating system's clipboard. Both of these critical work functions are inoperable from within a jupyter notebook and had to be culled in order to operate properly. 
> The machines-received repository is a "soft" fork of [ninjascripts](https://github.com/keith-flynn/ninjascripts/) and maintains the original upstream version's history.
---
##### Machine form factors: (**T**)ower, (**D**)esktop, (**S**)mall, (**U**)ltrasmall, (**M**)ini
##### - Though not pictured here, Mini is the only form factor this example CSV contains.
##### - They are typically less than half the size of an Ultrasmall form factor.
---
<img src="https://www.dell.com/community/image/serverpage/image-id/22944i9A5AA4C46F5980DE?v=v2" width="400"/>