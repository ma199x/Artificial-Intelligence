import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

df = pd.DataFrame({ 'from':['A', 'B', 'C','A','E','F','E','G','G','D','F'], 
'to':['D', 'A', 'E','C','A','F','G','D','B','G','C']})

plt.figure(1,figsize=(15,15)) # Build your graph
G=nx.from_pandas_edgelist(df, 'from', 'to')

# # Circular
# plt.subplot(221) 
# nx.draw_networkx(G, with_labels=True, node_size=500, node_color="red", pos=nx.circular_layout(G))
# plt.title("circular")

plt.subplot(221)
nx.draw_networkx(G,with_labels=True,pos=nx.kamada_kawai_layout(G))


# Random
plt.subplot(222)
nx.draw_networkx(G, with_labels=True, node_size=500, node_color="skyblue", pos=nx.random_layout(G))
plt.title("random")

# Spectral
plt.subplot(223)
nx.draw_networkx(G, with_labels=True, node_size=500, node_color="skyblue", pos=nx.spectral_layout(G))
plt.title("spectral")

#Spring 
plt.subplot(224)
nx.draw_networkx(G, with_labels=True, node_size=500, node_color="skyblue", pos=nx.spring_layout(G))
plt.show()