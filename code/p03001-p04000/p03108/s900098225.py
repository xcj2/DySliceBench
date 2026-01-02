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

def count_root(x):

    return parents[find(x)]

edges = []

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a,b))
parents = [-1] * N
ans = [0] * M
ans[-1] = N * (N-1) // 2

for i in range(M-1, 0, -1):
    c1, c2 = edges[i]

    if not same(c1, c2):
        ans[i-1] = ans[i] - count_root(c1) * count_root(c2)
        union(c1,c2)
    else:
        ans[i-1] = ans[i]     

for a in ans:
    print(a)