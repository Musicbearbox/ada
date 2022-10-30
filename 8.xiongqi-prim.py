#use adjecency list
#why undirected?
#use example 1
    #0,  1,  2,  3,  4
G={
    0:[[1,2],[2,2],[3,5],[4,3]],
    1:[[0,2],[2,1],[3,4],[4,4]],
    2:[[0,2],[1,1],[3,3],[4,5]],
    3:[[0,5],[1,4],[2,3],[4,9]],
    4:[[0,3],[1,4],[2,5],[3,9]]
}

#put all vertex into the queue
#for each vertex
#set key = infinity
INF = 999
r = 0

from heapdict import heapdict #pip install heapdict or conda install heapdict

Q = heapdict()
for i in G.keys():
    Q[i] = INF
Q[r] = 0

# print(f"Queue:{list(Q.items())}")
# u = Q.popitem()[0]  #why 0 ==> 0 refers to priority, 1 refers to the node
# print(f"Queue:{list(Q.items())}")
# u = Q.popitem()[0]  #why 0 ==> 0 refers to priority, 1 refers to the node
# print(f"Queue:{list(Q.items())}")
# u = Q.popitem()[0]  #why 0 ==> 0 refers to priority, 1 refers to the node

#set pi = NIL
pi = [None] * 5
# set the (pi of r) = -1 or anything you like
pi[r] = -1
print(f"Pi:{pi}")
#r.key = 0
#put all vertex into the queue

def adj( G, u):
    neighbors = []
    for key in G:
        each = G[key]
        neighbors.append ( each )
    return neighbors

def v_in_Q(Q,v):
    keys = list(Q.keys())
    #check if v in keys
    if v in keys:
        return True
    else:
        return False

#while q is not empty
while(Q):
    #u = extract_min (dic has no extract_min)
    u = Q.popitem()[0]  #node
    for node in G[u]:
    #node是key\value pair
    #for v in adj[u]
        if (v_in_Q(Q,node[0]) and node[1] < Q[node[0]]):
        #if v in Q, and w(u,v)<v.key
            pi[node[0]] = u
            #v.pi = u
            Q[node[0]] = node[1]
            #v.key = w(u,v)
print(f"Pi:{pi}")





#you have to suffer wrting your own min function ==>o(n)
    #priority queue can do extract_min in o(log n)
    #we should use heap!!!
    #this morning i already,there are three ways:
    #from Queue import priorityQueue(this one easiest, but not a dicctionary)
    #heapq: instead 0:0; 1:999 => 0:0;999:1
    #import heapdict (is our hero ,basically dict)