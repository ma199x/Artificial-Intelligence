import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.layout import circular_layout
g=nx.Graph()
g.add_node("1")
g.add_node("2")
g.add_node("3")
g.add_node("4")
g.add_node("5")
g.add_node("6")
g.add_node("7")
g.add_node("8")
nx.draw(g,pos=nx.random_layout(g),with_labels=1)
plt.show()