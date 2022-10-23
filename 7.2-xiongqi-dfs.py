#ajaacency list
#to find if there is a path from Thailand to China
graph = {
    'Thailand':['America','Vietnam'],
    'America':['China','Germany'],
    'UK':['Germany'],
    'Germany':['Vietnam'],
    'Nepal':['UK','Germany'],
    'Vietnam':[],
    'China':['Nepal']
}

visited = set()
found = False

def DFS( graph, s ,e):
    global found
    if(s == e):
        found = True
        print(s,"-->",end="") 
        print("\nyou can from "+ start +" to "+ end)
        return
    if s not in visited:
        print(s,"-->",end="")  
        visited.add(s)
        for next in graph[s]:
            DFS(graph, next,e)
            if(found == True):
                break
    
    
   
start = 'Thailand'
end = 'China'
DFS(graph, start ,end)
if(found == False):
        print("\nyou can not from "+ start +" to "+ end)



