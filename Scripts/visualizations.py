import matplotlib.pyplot as plt
from machines_received import POMassager

class ChartTime():

    # visuals
    plt.style.use('dark_background')
    df_sorted = POMassager.df.sort_values(by='COUNT', ascending=False)
    plt.figure(figsize=(10,7), dpi=80)
    plt.bar(df_sorted.MODEL, df_sorted.COUNT)
    plt.xticks(rotation=45, fontsize=13)
    plt.title('Machines Received', fontsize=20)
    plt.ylabel('Number of Machines', fontsize=13)
    plt.tight_layout()
    plt.show()

    # Make a percentage column for cost_vis df. Each item in total column / total of whole column * 100 to play nice with charting
    POMassager.cost_vis['TOTALPCT'] = POMassager.cost_vis.apply(lambda x: (x['TOTAL'] / POMassager.cost_vis['TOTAL'].sum()) * 100, axis=1)
    print("ChartTime test 1/1 : cost_vis again")
    print(POMassager.cost_vis)

    sorted_cost_vis = POMassager.cost_vis.sort_values(by='TOTALPCT', ascending=False)
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
    plt.title('Estimated Price: $' + POMassager.total_cost)
    ax1.axis('equal')
    plt.show()
