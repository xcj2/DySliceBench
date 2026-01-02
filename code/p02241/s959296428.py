import heapq

def root(x):
    path_to_root = []
    while P[x] != x:
        path_to_root.append(x)
        x = P[x]
    for node in path_to_root:
        P[node] = x
    return x
def is_same_set(x,y):
    return root(x) == root(y)
def unite(x,y):
    P[root(x)] = root(y)

W = 0
N = int(input().strip())
P = [i for i in range(N)]
A = []
for i in range(N):
    v = list(map(int,input().strip().split(' ')))
    A.append(v)
edges = [] 
for i in range(N):
    for j in range(i,N):
        edge = [A[i][j],i,j]
        heapq.heappush(edges,edge)
while len(edges) > 0:
    e = heapq.heappop(edges)
    I = e[1]
    J = e[2]
    if e[0] != -1:
        if not is_same_set(I,J):
            unite(I,J)
            W += e[0]
print(W)

