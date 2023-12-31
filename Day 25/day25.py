import networkx as nx
import matplotlib.pyplot as plt

with open("Day 25/input.txt", newline="") as file:
    components = file.read().splitlines()

components = {component.split(": ")[0]: component.split(": ")[1].split() for component in components}
print(components)

G = nx.Graph()

for component, connected_to in components.items():
    for node in connected_to:
        G.add_edge(component, node)

nx.draw(G, with_labels=True)
plt.show()

# nodes to cut:ex
# tqn-tvf
# tnr-vzb
# krx-lmg 

G.remove_edge("tqn", "tvf")
G.remove_edge("tnr", "vzb")
G.remove_edge("krx", "lmg")
subgraph_sizes = [len(c) for c in nx.connected_components(G)]
print(subgraph_sizes[0]*subgraph_sizes[1])