import sys
input = sys.stdin.readline
N, M = [int(x) for x in input().strip().split()]
p = [int(x) for x in input().strip().split()]
par = [i for i in range(N+1)]
rank = [0] * (N+1)

def find(x):
    if x == par[x]:
        return x
    par[x] = find(par[x])
    return par[x]

def isSame(x, y):
    return find(x) == find(y)

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 

    if rank[x] >= rank[y]:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
    else:
        par[x] = y

for m in range(M):
    x, y = [int(x) for x in input().strip().split()]
    union(x, y)

ans = 0
for i in range(1, N+1):
    if isSame(p[i-1], i):
        ans += 1
print(ans)