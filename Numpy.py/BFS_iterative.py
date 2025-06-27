'''BFS: 
It is an algorithm where we can start from the selected node and traverse the graph level-wise or layer wise,
thus exploring the neighbor nodes  and then moving on to the next level neighbor nodes.

As the name suggests:
1. We first move horizontally and visit all the nodes of the current layer.
2.Then moves to the next layer.

                Layer 0         O               Source node
                                /|\  
                               / | \   
                              /  |  \
                            1    2   3         
                           /\    |   /\   
                          /  \   |  /  \   
                        4     5  6 7   8                     ''' 

def bfs_iterative(graph,start):
    visited = set()
    queue = [start]
    while queue:
        node  = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])
graph = {
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':[],
    'E':[]
}         
bfs_iterative(graph,'A')