import numpy as np

def solve(n, x, y):
    def dist(i, j):
        return min(abs(x[i]-x[j]), abs(y[i]-y[j]))
    que = []
    for p in map(np.argsort, [x, y]):
        for i in range(n-1):
            u, v = p[i], p[i+1]
            que.append((u, v, dist(u, v)))
    parent = [i for i in range(n)]
    def find(i):
        if parent[i] == i:
            return i
        else:
            j = find(parent[i])
            parent[i] = j
            return j
    ans = 0
    for u, v, d in sorted(que, key=lambda _: _[2]):
        u = find(u)
        v = find(v)
        if u != v:
            ans += d
            if u > v:
                u, v = v, u
            parent[v] = u
    return ans

n = int(input())
x = np.zeros(n, dtype=int)
y = np.zeros(n, dtype=int)
for i in range(n):
    x[i], y[i] = map(int, input().split())
print(solve(n, x, y))