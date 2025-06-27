'''
Graph Terminolgy
Nodes are called Vertices, and the connections between them are called edges.
Two vertices are said to be adjacent if there exists a direct edge connecting the them.
The degree of a node is defined as the number of edges that are incident to it.
A path is a collection of edges through which we can reach from one node to the other node in a graph.
A graph is said to be connected if there is a path between every pair of vertices.
'''

'''The minimum number of edges in a connected graph will be (N-1) where N is the number of nodes.
In a complete graph ,there are nC2 number of edges means (N*(N-1))/2 edges,where n is the number of nodes.
This is the maximum number of edges that a graph can have.
'''
'''DFS: DEPTH FIRST SEARCH
It is a graph traversal algorithm that starts from a source node and explores as far as possible along each 
branch before backtracking
It uses a stack and goes deep into one track before trying others. '''