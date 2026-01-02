#template
def inputlist(): return [int(j) for j in input().split()]
from collections import Counter
#template
#issueから始める
#Union Find
N,M,K = inputlist()
graph = [[] for _ in range(N)]
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

#初期化
#根なら-size,子なら親の頂点
par = [-1]*(N)
for i in range(M):
    A,B = inputlist()
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)
    unite(A-1,B-1)
bgraph = [[] for _ in range(N)]
for i in range(K):
    C,D = inputlist()
    if same(C-1,D-1):
        bgraph[C-1].append(D-1)
        bgraph[D-1].append(C-1)
li = [0]*N
for i in range(N):
    k = size(i)
    n = len(graph[i])
    m = len(bgraph[i])
    li[i] = k-n-m-1
print(*li)