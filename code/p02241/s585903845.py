N = int(input())

ep = []
for i in range (N):
    a = list(map(int,input().strip().split()))
    for j in range(i,N):
        if a[j] != -1:
            ep.append([a[j],i,j])

P = [i for i in range(N)]
def root(x):
    path_to_root = []
    while P[x] != x:
        path_to_root.append(x)
        x = P[x]
    for node in path_to_root:
        P[node] = x # パス圧縮
    return x
def is_same_set(x,y):
    return root(x) == root(y)
def unite(x,y):
    P[root(x)] = root(y)

ep.sort()
T = []
ans = 0
for e in ep:
    if is_same_set(e[1],e[2]) == False:
        ans += e[0]
        unite(e[1],e[2])
print(ans)

