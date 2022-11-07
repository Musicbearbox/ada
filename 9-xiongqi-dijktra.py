#dijktra
    
#use example 1
    #0,  1,  2,  3,  4  5  6  7  8
G=[
    [0 , 4 , 0 , 0 , 0, 0, 0, 8, 0],   #0
    [4 , 0 , 8 , 0 , 0, 0, 0, 11 , 0],   #1
    [0 , 8 , 0 , 7 , 0, 4, 0, 0 , 2],    #2
    [0 , 0 , 7 , 0 , 9, 14, 0, 0 , 0],   #3
    [0 , 0 , 0 , 9 , 0, 10, 0, 0 , 0],   #4
    [0 , 0 , 4 , 14 , 10, 0, 2, 0 , 0],   #5
    [0 , 0 , 0 , 0 , 0, 2, 0, 1 , 6],   #6
    [8 , 11 , 0 , 0 , 0, 0, 1, 0 , 7],   #7
    [0 , 0 , 2 , 0 , 0, 0, 6, 7 , 0]   #8                                   
    ]

#put all vertex into the queue
#for each vertex
#set key = infinity
INF = 999
N = 9
r = 0

from heapdict import heapdict #pip install heapdict or conda install heapdict

Q = heapdict()
for i in range(N):
    Q[i] = INF
Q[r] = 0

# print(f"Queue:{list(Q.items())}")
# u = Q.popitem()[0]  #why 0 ==> 0 refers to priority, 1 refers to the node
# print(f"Queue:{list(Q.items())}")
# u = Q.popitem()[0]  #why 0 ==> 0 refers to priority, 1 refers to the node
# print(f"Queue:{list(Q.items())}")
# u = Q.popitem()[0]  #why 0 ==> 0 refers to priority, 1 refers to the node

#set pi = NIL
pi = [None] * N
# set the (pi of r) = -1 or anything you like
pi[r] = -1
print(f"Pi:{pi}")
#r.key = 0
#put all vertex into the queue

def adj( G, u):
    neighbors = []
    for index in range(len(G)):
        each = G[index]
        if each[u]!=0: 
            neighbors.append ( index )
    return neighbors

def v_in_Q(Q,v):
    keys = list(Q.keys())
    #check if v in keys
    if v in keys:
        return True
    else:
        return False

# test = []
#while q is not empty
while(Q):
    #u = extract_min (dic has no extract_min)
    #get minimal node's value
    node = Q.popitem()  #node
    u = node[0]
    # test.append(u)
    for v in adj(G,u):
    #for v in adj[u]
        if (v_in_Q(Q,v) and (G[u][v]+node[1]) < Q[v]):
            pi[v] = u
            Q[v] = G[u][v]+node[1]

print(pi)
# print(test)