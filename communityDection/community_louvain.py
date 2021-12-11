import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx
import json

input1 = open('politicsEdge.json')
Edges = json.load(input1)
input1.close()


input2 = open('politicsLeaning.json')
Leaning = json.load(input2)
input2.close()

G = nx.Graph()
for edge in Edges:
	for key in edge.keys():
		G.add_edge(key, edge[key])
		#print(key,' ', edge[key])

#first compute the best partition
partition = community_louvain.best_partition(G)

# compute the best partition
partition = community_louvain.best_partition(G)

# draw the graph
pos = nx.spring_layout(G)
# color the nodes according to their partition
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
                       cmap=cmap, node_color=list(Leaning.values()))
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()
