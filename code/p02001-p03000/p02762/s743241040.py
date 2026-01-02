import sys
from itertools import accumulate
n, m, k = [int(i) for i in sys.stdin.readline().split()]

par = list(range(n))
ns = [1 for i in range(n)]

def find(x):
    ls = []
    while x != par[x]:
        ls.append(x)
        x = par[x]
    for l in ls:
        par[l] = x
    return x

def unite(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        par[x] = y
        ns[y] += ns[x]

def is_same(x, y):
    if find(x) == find(y):
        return True
    else:
        return False

ls = [0 for i in range(n)]
friends = [0 for i in range(n-1)]

for i in range(m):
    a, b = [int(i) for i in sys.stdin.readline().split()]
    a -= 1
    b -= 1
    ls[a] -= 1
    ls[b] -= 1
    unite(a, b)

for i in range(n):
    root = find(i)
    ls[i] += ns[root]


for i in range(k):
    c, d = [int(i) for i in sys.stdin.readline().split()]
    c -= 1
    d -= 1
    if is_same(c, d):
        ls[c] -= 1
        ls[d] -= 1

print(" ".join([str(i - 1) for i in ls]))