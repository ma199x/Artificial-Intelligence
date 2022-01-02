# import networkx as nx
# import matplotlib.pyplot as plt
# import pandas as pd

# G=nx.DiGraph()
# G1=nx.DiGraph()
# G1.add_edge('A', 'B',weight=5)
# G1.add_edge('B', 'C', weight=2)
# G1.add_edge('A', 'C', weight=10)
# G.add_edge('C', 'G',weight=4)
# G.add_edge('G', 'E', weight=3)
# G.add_edge('B', 'E', weight=1)
# G.add_edge('D', 'B', weight=1)
# G.add_edge('D', 'E', weight=4)
# G.add_edge('S', 'A',weight=3)
# G.add_edge('S', 'D', weight=2)
# # labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx(G,pos=nx.circular_layout(G),node_color="green",with_labels=True)
# # nx.draw_networkx(G1,pos=nx.circular_layout(G),node_color="green",with_labels=True)
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
d={
    'from':[1,2,3],
    'to': [2,4,5]
}
df=pd.DataFrame(d)
print(df)