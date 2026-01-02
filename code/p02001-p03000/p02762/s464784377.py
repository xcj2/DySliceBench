import sys
input = sys.stdin.readline

#Union Find

#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]

N, M, K = map(int, input().split())
par = [-1 for i in range(N)]
rank = [0] * N
frendCnt = [0] * N
bloc = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    frendCnt[a] += 1
    frendCnt[b] += 1
    unite(a, b)

for i in range(K):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    bloc[c].append(d)
    bloc[d].append(c)

for i in range(N):
    ans = size(i) - frendCnt[i] - 1
    for j in bloc[i]:
      if same(i, j):
           ans -= 1
    print(ans, end=' ')