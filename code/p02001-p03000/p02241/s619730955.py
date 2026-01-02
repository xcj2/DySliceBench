def root(x):
    path_to_root = []
    while x != P[x]:
        path_to_root.append(x)
        x = P[x]
    for node in path_to_root:
        P[node]=x
    return x

def unite(x,y):
    P[root(x)] = root(y)

def is_same_set(x,y):
    return root(x) == root(y)

n = int(input())
P = [i for i in range(n)]
length=[]
points=[]
for i in range(n):
    length.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i,n):
        if length[i][j] != -1:
            points.append((i,j,length[i][j]))
	
points.sort(key=lambda x:x[2])

totalweight = 0
for p in points:
    i,j,w = p
    if not is_same_set(i,j):
       totalweight += w
       unite(i,j)

print(totalweight)
