from collections import defaultdict, Counter
import sys

def root(uft, x):
    if uft[x] == x: return x
    uft[x] = root(uft, uft[x])
    return uft[x]

def union(uft, rank, x, y):
    x = root(uft, x)
    y = root(uft, y)
    if x == y:
        return

    if rank[x] >= rank[y]:
        uft[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
    else:
        uft[x] = y

def same(uft, x, y):
    return root(uft, x) == root(uft, y)

def answer():
    n, m, k = map(int, input().split())
    friend = defaultdict(int)
    block = defaultdict(int)
    group = defaultdict(set)
    uft = [i for i in range(n+1)]
    rank = [0] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        union(uft, rank, a, b)
        friend[a] += 1
        friend[b] += 1
    for j in range(k):
        c, d = map(int, input().split())
        if not same(uft, c, d):
            continue
        block[c] += 1
        block[d] += 1
    for i in range(1, n+1):
        root(uft, i)
    c = Counter(uft)
    return [c[uft[i]]-block[i]-friend[i]-1 for i in range(1, n+1)]

print(*answer())

