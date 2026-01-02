from sys import stdin
n, m = map(int, stdin.readline().split())
G = [-1] * n
def root(x):
    if G[x] < 0: return x
    G[x] = root(G[x])
    return G[x]
def uniteSet(x, y):
    x = root(x)
    y = root(y)
    if x == y : return
    if G[x] > G[y] : x, y = y, x
    G[y] = x
def findSet(x, y):
    return root(x) == root(y)
for i in range(0, m):
    s, t = map(int, stdin.readline().split())
    uniteSet(s, t)
q = int(stdin.readline())
for i in range(0, q):
    s, t = map(int, stdin.readline().split())
    print("yes" if findSet(s, t) else "no")