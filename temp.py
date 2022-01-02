# Q1 
# # 1
# D={
#     'name':'ali',
#     'age':18,
#     'f_color':{1:'black',2:'rad'}
# }
# D["f_color"][2]="blue"
# print(D)

# 2-
# l=[1,2,7,4]
# l.remove(2)
# print(l)

# 3-
# 0   1   2   3   4   5   6
# t=('A','B','D','T','H','S','K')
# print(t[1::2])

# 4-
# s={1,0.5,"hellow"}
# s.clear()
# print(s)

# 5-
# num=[1,2,3,4,5,6,7]
# num2=[n*2 for n in num if n%2!=0]
# print(num2)

# Q2
from networkx.drawing.layout import circular_layout, kamada_kawai_layout
from networkx.drawing.nx_pylab import draw
import pandas as pd 
import matplotlib.pyplot as plt
import networkx as nx

graph={
    1:['y1','y1','x4','x1','z3','z1','y1','x4'],
    2: ['y3','x4','x1','z3','z1','y3','z3','z1'] 
}
df=pd.DataFrame(graph)
g=nx.from_pandas_edgelist(df,1,2)
nx.draw_networkx(g,pos=kamada_kawai_layout(g),with_labels=True,node_size=1500)
plt.show()
# print(df)