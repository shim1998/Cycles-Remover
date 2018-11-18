import networkx as nx
from load import *
import matplotlib.pyplot as plt

def visualise(path,x,y,output):
    G=nx.DiGraph()
    nodes=[i for i in range(0,6302)]
    data=loaddata(path)
    data=data.split('\n')
    edges=[]
    for i in data:
        if '#' not in i:
            edges.append(i.split('\t'))
    edges.pop()
    for i in range(0,len(edges)):
        edges[i][0]=int(edges[i][0])
        edges[i][1]=int(edges[i][1])
    G=nx.DiGraph()
    G.add_nodes_from(nodes[x:y])
    G.add_edges_from(edges[x:y])
    nx.draw_random(G)
    plt.savefig(output)
