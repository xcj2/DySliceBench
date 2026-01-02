#union-find-tree
import sys
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

n, q = map(int, input().split())
union_find_lis = init(n-1)
for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        union(union_find_lis, x, y)
    else:
        if sameset(union_find_lis, x, y):
            print(1)
        else:
            print(0)
