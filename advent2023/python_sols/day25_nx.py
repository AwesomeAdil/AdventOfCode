import networkx as nx
import matplotlib.pyplot as plt
raw_data = open('sample.txt', 'r').read()
data = raw_data.split('\n')[:-1]
G = nx.Graph()
#G = nx.DiGraph()
for line in data:
    parts = line.split(': ')
    for x in parts[-1].split():
        G.add_edge(parts[0], x)
        #G.add_edge(parts[0], x, {'capacity':1})

nx.draw_spring(G, with_labels=True)
plt.show()

"""
nx.remove_edge('tmt', 'pnz')
nx.remove_edge('gbc', 'hrz')
nx.remove_edge('mvv', 'xkz')
""" 

