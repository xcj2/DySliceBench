import sys
import collections
sys.setrecursionlimit(10**7)


def init(n):
    return list(range(n+1))

def find(lis, x):
    if lis[x] == x:
        return x
    else:
        lis[x] = find(lis, lis[x])
        return lis[x]

def sameset(lis, x, y):
    return find(lis, x) == find(lis, y)

def union(lis, x, y):
    x = find(lis, x)
    y = find(lis, y)
    if x != y:
        lis[x] = y

V,E=map(int,input().split())
union_find_tree = init(V)
graph = []
for _ in range(E):
    s, t, w = map(int, input().split())
    graph.append((s,t,w))

cost = 0
for (s,t,w) in sorted(graph, key=lambda x: x[2]):
    if not sameset(union_find_tree,s,t):
        union(union_find_tree,s,t)
        cost += w
print(cost)
