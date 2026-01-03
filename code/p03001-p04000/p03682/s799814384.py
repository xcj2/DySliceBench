N = int(input())
rec = []
for i in range(N):
    x, y = map(int, input().split())
    rec.append((i, x, y))

recx = sorted(rec, key=lambda s: s[1])
recy = sorted(rec, key=lambda s: s[2])

G = []
for i in range(1, N):
    costx = min(abs(recx[i][1] - recx[i - 1][1]), abs(recx[i][2] - recx[i - 1][2]))
    costy = min(abs(recy[i][1] - recy[i - 1][1]), abs(recy[i][2] - recy[i - 1][2]))
    G.append((recx[i][0], recx[i - 1][0], costx))
    G.append((recy[i][0], recy[i - 1][0], costy))

rank = [0] * N
par = [i for i in range(N)]


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] > rank[y]:
        par[y] = x
    else:
        par[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def same(x, y):
    return find(x) == find(y)


G = sorted(G, key=lambda s: s[2])
num = 0
for e in G:
    if not same(e[0], e[1]):
        unite(e[0], e[1])
        num += e[2]

print(num)
