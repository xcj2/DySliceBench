N, M = (int(i) for i in input().split())
uf = [-1]*N
def parent(v):
    if uf[v] < 0:
        return v
    else:
        uf[v] = parent(uf[v])
        return uf[v]

def size(v):
    return -uf[parent(v)]

def union(u, v):
    pu = parent(u)
    pv = parent(v)
    if pu != pv:
        res = uf[pv] * uf[pu] #適当な返り値
        uf[pv] += uf[pu]
        uf[pu] = pv
    else:
        res = 0
    return res

for i in range(M):
    X, Y, Z = (int(i) for i in input().split())
    union(X-1, Y-1)
ans = 0
for i in range(N):
    if uf[i] < 0:
        ans += 1
print(ans)