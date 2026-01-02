from sys import stdin
N,M = [int(x) for x in stdin.readline().rstrip().split()]
P = [int(x) for x in stdin.readline().rstrip().split()]
par = [i for i in range(N+1)]
rank = [0] * (N+1)
 
def find(x):
    if par[x] == x:
        return par[x]
    else:
        par[x] = find(par[x])
        return par[x]
 
def union(x,y):
    x = find(x)
    y = find(y)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
 
def check_same(x,y):
    return find(x) == find(y)
 
for _ in range(M):
    x,y = [int(x) for x in stdin.readline().rstrip().split()]
    union(x,y)
ans = 0
for i in range(1,N+1):
    if find(i) == find(P[i-1]):
        ans += 1
print(ans)