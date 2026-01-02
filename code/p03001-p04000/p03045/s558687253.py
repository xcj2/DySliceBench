def solve(n, m, x, y, z):
    parent = {i: i for i in range(1, n+1)}
    def find(v):
        if v == parent[v]:
            return v
        else:
            return find(parent[v])
    def union(u, v):
        u = find(u)
        v = find(v)
        if u > v:
            u, v = v, u
        parent[v] = u
    for i in range(m):
        union(x[i], y[i])
    return len(set([find(v) for v in parent.keys()]))

n, m = map(int, input().split())
x = [0] * m
y = [0] * m
z = [0] * m
for i in range(m):
    x[i], y[i], z[i] = map(int, input().split())
print(solve(n, m, x, y, z))