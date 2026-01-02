n = int(input())
m = []

for _ in range(n):
    tmp = [int(x) for x in input().split()]
    m.append(tmp)

#辺を全て持つリストを作る
edge_list = [] 
j = 1
for i in range(n-1):
    for k,x in enumerate(m[i][j:]):
        if x != -1:
            edge_list.append((x,i,k+j))
        else:
            pass
    j += 1
edge_list.sort()

root_list = [i for i in range(n)]

def root(x):
    path_to_root = []
    while root_list[x] != x:
        path_to_root.append(x)
        x = root_list[x]
    for node in path_to_root:
        root_list[node] = x
    return x

def is_same_root(x,y):
    return root(x) == root(y)

def unite(x,y):
    root_list[root(x)] = root(y)

cost = 0
for x in edge_list:
    w,p,q = x
    if is_same_root(p,q):
        continue
    else:
        cost += w
        unite(p,q)

print(cost)

