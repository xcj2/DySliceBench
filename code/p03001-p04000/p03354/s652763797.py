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

N, M = map(int, input().split())
union_find_lis = init(N)
P = [0] + [int(s) for s in input().split()]
for _ in range(M):
    x, y = map(int, input().split())
    union(union_find_lis, x, y)
count = 0
for index in range(1, N+1):
    if sameset(union_find_lis, P[index], index):
        count += 1
print(count)