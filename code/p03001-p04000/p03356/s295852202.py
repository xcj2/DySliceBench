N,M = map(int,input().split())
p = [int(i) for i in input().split()]
xy = []

for _ in range(M):
    xy.append(list(map(int,input().split())))

par = [0 for _ in range(N+1)]
rank = [0 for _ in range(N+1)]

def init(n):
    for i in range(n):
        par[i] = i
        rank[i] = 0
def find(x):
    if par[x] ==x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
def unite(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

def same(x,y):
    return True if find(x) == find(y) else False

init(N+1)
for x,y in xy:
    unite(x,y)
count = 0
for i in p:
    if same(i,p[i-1]):
        count += 1
print(count)