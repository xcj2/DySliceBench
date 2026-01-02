h, w = map(int, input().split())
S = [str(input()) for _ in range(h)]

#g = [[] for _ in range(h*w)]

n = h*w

def Find(x, par):
    if par[x] < 0:
        return x
    else:
        par[x] = Find(par[x], par)
        return par[x]

def Unite(x, y, par, rank):
    x = Find(x, par)
    y = Find(y, par)

    if x != y:
        if rank[x] < rank[y]:
            par[y] += par[x]
            par[x] = y
        else:
            par[x] += par[y]
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

def Same(x, y, par):
    return Find(x, par) == Find(y, par)

def Size(x, par):
    return -par[Find(x, par)]

par = [-1]* n
rank = [0]*n

for y in range(h):
    for x in range(w):
        idx1 = y*w+x
        for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < h and 0 <= nx < w:
                idx2 = ny*w+nx
                if S[y][x] != S[ny][nx]:
                    Unite(idx1, idx2, par, rank)

ans = 0
#print(par)
X = [[0, 0] for _ in range(n)]
K = []

for i in range(n):
    y, x = divmod(i, w)
    if par[i] < 0:
        K.append(i)
        if S[y][x] == '#':
            X[i][0] += 1
        else:
            X[i][1] += 1
    else:
        if S[y][x] == '#':
            X[Find(i, par)][0] += 1
        else:
            X[Find(i, par)][1] += 1

ans = 0
for k in K:
    ans += X[k][0]*X[k][1]
print(ans)