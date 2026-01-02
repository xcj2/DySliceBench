import sys
readline = sys.stdin.readline

def root(x):
    if uf[x] == x:
        return x
    else:
        uf[x] = root(uf[x])
        return uf[x]

def same(x, y):
    return root(x) == root(y)

def unite(x, y):
    rx = root(x)
    ry = root(y)
    if rx == ry:
        return
    uf[rx] = ry

N, M = map(int,readline().split())
p = list(map(int,readline().split()))
p.insert(0, -1)
uf = [i for i in range(N+1)]
for i in range(M):
    a, b = (map(int,readline().split()))
    unite(a, b)
for i in range(1, N+1):
    root(i)

ans = 0
#戒めコード
#N += 1
#match = [[] for i in range(N)]
#for i in range(1, N):
#    match[uf[i]].append(i)
#for i in range(1, N):
#    matchlen = len(match[i])
#    for j in range(matchlen):
#        if p[match[i][j]] in match[i]:
#            ans += 1

for i in range(1, N+1):
    if same(i, p[i]):
        ans += 1
print(str(ans))

#root(i)=root(j)ならばiとjは行き来できる(iはjの居る場所に到達できる)
#知りたいのはiがp[i]のいる位置に来れるかどうか
#root(i)=root(p[i])なら,iはp[i]の位置に来れる,すなわちi番目にiを持ってくることができる