import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import accumulate

N, M = map(int, input().split())


def find(x):
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]    

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    if x > y:
        x, y = y, x

    parents[x] += parents[y]
    parents[y] = x    

def same(x,y):

    return find(x) == find(y)

edges = []
ans = 0
for i in range(M):
    a, b = map(int, input().split())
    edges.append((a-1, b-1))

for i in range(M):
    parents = [-1] * N
    tmp1, tmp2 = edges[i]
    for j in range(M):
        if i == j: continue
        a,b = edges[j]
        union(a,b)

    if not same(tmp1, tmp2):
        ans += 1

print(ans)