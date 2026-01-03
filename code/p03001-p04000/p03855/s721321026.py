import sys
sys.setrecursionlimit(10**7)

road_par = []
road_rank = []
rail_par = []
rail_rank = []
c1 = []
c2 = []

def init(par, rank, c, n):
    for i in range(n):
        par.append(i)
        rank.append(0)
        c.append(0)


def find(par,x):
    if par[x] == x:
        return x
    par[x] = find(par, par[x])
    return par[x]


def unite(par, rank, x, y):
    x = find(par, x); y = find(par, y)
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y
    elif rank[y] < rank[x]:
        par[y] = x
    else:
        par[y] = x
        rank[x] += 1


N, K, L = map(int, input().split())
init(road_par, road_rank, c1, N)
init(rail_par, rail_rank, c2, N)


for i in range(K):
    f, t = map(int, input().split())
    unite(road_par, road_rank, f-1, t-1)

for i in range(L):
    f,t = map(int, input().split())
    unite(rail_par, rail_rank, f-1, t-1)

for i in range(N):
    c1[find(road_par, i)] += 1
    c2[find(rail_par, i)] += 1

ans = [0 for i in range(N)]

"""
for i in range(N):
    for j in range(N):
        if find(road_par, i) == find(road_par, j) and find(rail_par, i) == find(rail_par, j):
            ans[i] += 1
"""
from collections import defaultdict
ans = defaultdict(int)
for i in range(N):
    ans[(find(road_par, i), find(rail_par, i))] += 1

for i in range(N):
    print(ans[(find(road_par, i), find(rail_par, i))], end=' ')
print('')