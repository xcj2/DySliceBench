import sys
from collections import Counter
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M, K = [int(x) for x in input().strip().split()]

# 友達グループ(候補含む)
par = [i for i in range(N+1)]
rank = [0] * (N+1)

# 友達
friends = [0 for _ in range(N+1)]

# ブロックしている数
blocked = [0 for _ in range(N+1)]

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
    a, b = [int(x) for x in input().strip().split()]
    union(a, b)
    friends[a] += 1
    friends[b] += 1

for k in range(K):
    c, d = [int(x) for x in input().strip().split()]
    if isSame(c, d):
        blocked[c] += 1
        blocked[d] += 1


for n in range(1, N+1):
    find(n)

cnt = Counter(par)
print(*[cnt[par[n]] - friends[n] - blocked[n] - 1 for n in range(1, N+1)])