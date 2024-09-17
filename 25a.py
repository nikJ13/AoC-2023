# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:01:21 2024

@author: niket
"""

import networkx as net

graph = net.Graph()  #initialise an undirected graph

file1 = open('input25.txt')
Lines = file1.readlines()

for line in Lines:
    #print(line)
    source,destination = line.strip().split(": ")
    for nodes in destination.split():
        graph.add_edge(source,nodes)  #add the edges; since the graph is undirected, both the vertices should be added
        graph.add_edge(nodes,source)  #in this manner

print(graph)

#print(net.minimum_edge_cut(graph)) #this function returns a set of edges that have to be cut to give two graphs

# removing the above mentioned edges

graph.remove_edges_from(net.minimum_edge_cut(graph))

print(graph)

print(*net.connected_components(graph))

one, two = net.connected_components(graph)

print(len(one)*len(two))

