#ajaacency matrix
from ast import Try

graph= [
    [-1,True,False,False,False,True,False],
    [False,-1,False,True,False,False,True],
    [False,False,-1,True,False,False,False],
    [False,False,False,-1,False,True,False],
    [False,False,True,True,-1,False,False],
    [False,False,False,False,False,-1,False],
    [False,False,False,False,True,False,-1]
]

def BFS( graph, s ):
    visited = set()
    queue = set() 
    visited.add(s) #means make it black
    queue.add(s)

    while queue: #as long as the queue is not empty..
        u = queue.pop()
        print(u,"-->",end="")
        for index in range(len(graph[u])):
            result = graph[u][index]
            if(result):
                if index not in visited:
                    visited.add(index)    
                    queue.add(index)


BFS(graph,0)



