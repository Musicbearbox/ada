#ajaacency matrix

graph= [
    [-1,True,False,False,False,True,False],
    [False,-1,False,True,False,False,True],
    [False,False,-1,True,False,False,False],
    [False,False,False,-1,False,True,False],
    [False,False,True,True,-1,False,False],
    [False,False,False,False,False,-1,False],
    [False,False,False,False,True,False,-1]
]

visited = set()

def DFS( graph, s ):
    if s not in visited:
        print(s,"-->",end="")  
        visited.add(s)
        for index in range(len(graph[s])):
            neighbor = graph[s][index]
            if(neighbor):
                DFS(graph, index)


DFS(graph,0)



