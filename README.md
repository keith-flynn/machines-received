# Machines Received

## Automate purchase order data visualizations

---

## Project Overview:
- Imports raw price data and cleans
- Imports purchase order data and cleans
- Merges dataframes 
- Produces useful information about purchase orders
- Generates two visualizations:
  - Bar graph of machine types received by total units
  - Pie chart of which models account for total cost

---

**Code and Resources Used**
 - Python 3.9+
   - _Pandas_
   - _Matplotlib_
 - Jupyter Notebook 6.4.12+
 - From the command line, input `pip install -r requirements.txt` from within the project directory to add required modules.

---

### **To Run:**

The work is presented in [machines-received.ipynb](machines-received.ipynb)

Launch Jupyter Notebook and navigate to the corresponding machines-received.ipynb file in the main folder of the repository.

*If the user prefers to simply execute the script without reading all of the comments:*

Windows:

- from command line within the 'Scripts' directory, input `python -m main.py`

Linux/MacOS:

- from bash within the 'Scripts' directory, input `python3 main.py`

---

### **The Basics:**

1. In Part 1 we import a CSV file with cost information for the different models of personal computers that we will be working with. This information is cleaned and analyzed to become a dataframe to reference in Part 2.

2. In Part 2 we import a CSV file with a batch of machines that have just been received into the system. This data is cleaned and analyzed before importing prices from the dataframe in Part 1.

3. The data is then analyzed and represented by two visualizations

**The Jupyter Notebook is arranged in a very procedural presentation, and dataframes are printed liberally to demonstrate the changes which are occurring.**

The presentation is displayed neatly in the Jupyter Notebook. The raw code has been refactored and modularized if the user prefers execution from the REPL.

---

*Some helpful terminology:*

- **Purchase Order:** The batch of machines received under the same purchasing agreement. Purchase Orders are one of the means by which machines are tracked and accounting is calculated.
- **SKU:** Stock Keeping Unit. This is a retail industry term for a unit of something that is being sold. SKUs are similar to UPCs (bar codes) in that they represent the item being sold in a market's database.

  - In this program "SKU" will refer to the SKU's title, which will be a string. Example: 9020-M-I5
  - Every product you buy from your local grocer to Amazon's marketplace has a corresponding SKU number attached to it that is kept track of by sales and inventory systems.

---
---
### ***Project Features:***

[Full project feature fulfillment is documented in requirement-fulfillment.md](requirement-fulfillment.md)

1. Read in data from a local CSV
2. Use built-in Python, Pandas, functions/lambdas to manipulate data
3. Analyze with built-in Python/Pandas and custum functions
4. Make basic plots with Matplotlib
5. Markdown cells in Jupyter Notebook explaining throught process and code
---
### **In Detail:**
 A cost basis CSV is first cleaned to be universally applicable to machines in their receiving format. Data from a received purchase order is then imported, cleaned, and made into a dataframe visualizing its makeup by number of machines. Cost values from the cost basis CSV are then merged to create a visualization breakdown by model. The machines are then totaled by value using the averaged price, and a second visualization displays the projected average cost, along with a percentage representation of each model received.

---
---
#### *Sample Visualizations*:
![sample-bar](./assets/readme-img-source/sample-bar.png)
![sample-pie](./assets/readme-img-source/sample-pie.png)
---
---
##### This final project for Code Kentucky Data Analysis I is a continuation of my functional work program [ninjascripts](https://github.com/keith-flynn/ninjascripts/). My latest edition includes a file browser GUI to select which CSV file to import, and a section which automatically copies all of the serial numbers to the [system agnostic] operating system's clipboard. Both of these critical work functions are inoperable from within a Jupyter Notebook and had to be culled in order to operate properly. 
> The machines-received repository is a "soft" fork of [ninjascripts](https://github.com/keith-flynn/ninjascripts/) and maintains the original upstream version's history.
---
##### **Machine form factors from smallest to largest:**
##### (**M**)ini, (**U**)ltrasmall, (**S**)mall,  (**D**)esktop, (**T**)ower
##### *- First image: Ultrasmall, Small, Desktop, and Tower models 2009-2012*
##### *- Second image: Mini, Ultrasmall, Small models 2012-2020*
---
![sample-usdt](./assets/readme-img-source/sample-form-factors.png)
![sample-msd](./assets/readme-img-source/sample-form-factors2.png)
---
---
## License
[GNU GENERAL PUBLIC LICENSE](LICENSE)