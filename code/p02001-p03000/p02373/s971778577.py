# 参考　https://tjkendev.github.io/procon-library/python/graph/lca-segment-tree.html

# N: 頂点数
# G[v]: 頂点vの子頂点 (親頂点は含まない)

import sys
sys.setrecursionlimit(10**7)

N = int(input())
G = [[] for _ in range(N)]
for v in range(N):
    for j, nv in enumerate(map(int, input().split())):
        if j == 0:
            continue
        G[v].append(nv)  

# Euler Tour の構築
S = []
F = [0]*N
depth = [0]*N
def dfs(v, d):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    for w in G[v]:
        dfs(w, d+1)
        S.append(v)
dfs(0, 0)

# 存在しない範囲は深さが他よりも大きくなるようにする
INF = (N, None)

# LCAを計算するクエリの前計算
M = 2*N
M0 = 2**(M-1).bit_length()
data = [INF]*(2*M0)
for i, v in enumerate(S):
    data[M0-1+i] = (depth[v], i)
for i in range(M0-2, -1, -1):
    data[i] = min(data[2*i+1], data[2*i+2])

# LCAの計算 (generatorで最小値を求める)
def _query(a, b):
    yield INF
    a += M0; b += M0
    while a < b:
        if b & 1:
            b -= 1
            yield data[b-1]
        if a & 1:
            yield data[a-1]
            a += 1
        a >>= 1; b >>= 1

# LCAの計算 (外から呼び出す関数)
def query(u, v):
    fu = F[u]; fv = F[v]
    if fu > fv:
        fu, fv = fv, fu
    return S[min(_query(fu, fv + 1))[1]]

ans_list = []

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    ans = query(u, v)
    ans_list.append(ans)

print(*ans_list, sep="\n")
