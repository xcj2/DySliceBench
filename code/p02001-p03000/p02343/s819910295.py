from sys import stdin
high = [0] * 10000
par = [i for i in range(10000)]
def findSet(x):
    if par[x] == x: return x
    par[x] = findSet(par[x])
    return par[x]
def unite(x, y):
    x = findSet(x)
    y = findSet(y)
    if x == y: return
    if high[x] > high[y]: par[y] = x;
    else:
        par[x] = y
        if high[x] == high[y]: high[y] += 1
def same(x, y):
    return findSet(x) == findSet(y)
n, q = map(int, stdin.readline().split())
ans = []
ans_append = ans.append
for i in range(q):
    t, a, b = map(int, stdin.readline().split())
    if t == 0: unite(a, b);
    elif t == 1: ans_append(1 if same(a, b) else 0)
print(*ans, sep='\n')