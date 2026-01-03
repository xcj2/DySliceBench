import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
from collections import defaultdict
ns = defaultdict(set)
for i in range(n-1):
    u,v,c = map(int, input().split())
    u -= 1
    v -= 1
    ns[u].add((c,v))
    ns[v].add((c,u))
# print(ns)
k = len(bin(n-1))-2
# 深さ
def cdepth(root=0):
    # rootを根としたときの深さ
    ps = [None] * n
    ps[0] = -1
    q = [0]
    while q:
        u = q.pop()
        for c,v in ns[u]:
            if ps[v] is None:
                ps[v] = u
                q.append(v)
    # psを元から持っている場合、引数のnsをpsにしてこの下だけで良い
    depth = [None] * n
    depth[root] = 0
    q = [root]
    while q:
        u = q.pop()
        for c,v in ns[u]:
            if depth[v] is None:
                depth[v] = depth[u] + 1
                q.append(v)
    return depth, ps
def dijkstra(start):
    import heapq
    vals = [None] * n
    h = [(0, start)] # (距離, ノード番号)
    vals[start] = 0
    while h:
        val, u = heapq.heappop(h)
        for d, v in ns[u]:
            if vals[v] is None or vals[v]>val+d:
                vals[v] = val+d
                heapq.heappush(h, (vals[v], v))
    return vals

# ダブリング
def double(ps):
    # global: n=psのサイズ
    k = 0
    while pow(2,k)<n:
        k += 1
    prev = [[None]*n for _ in range(k)] # ノードjから2^i個上の上司
    for j in range(n):
        prev[0][j] = ps[j]
    for i in range(1,k):
        for j in range(n):
            p = prev[i-1][j]
            if p>=0:
                prev[i][j] = prev[i-1][p]
            else:
                prev[i][j] = p
    return prev
            

# k: 必要桁数を定める必要アリ
def cprev(u,i):
    """uからi個上の頂点を返す
    """
    for j in range(k):
        if i>>j&1:
            u = prev[j][u]
    return u

# k: 必要桁数を定める必要アリ
def lca(u,v):
    if depth[u]<depth[v]:
        v = cprev(v, depth[v]-depth[u])
    else:
        u = cprev(u, depth[u]-depth[v])
    if u==v:
        return u
    for i in range(k-1, -1, -1):
        if prev[i][u]!=prev[i][v]:
            u = prev[i][u]
            v = prev[i][v]
    return prev[0][u]

dist = dijkstra(0)
depth, ps = cdepth(0)
prev = double(ps)
q,K = map(int, input().split())
K -= 1
ans = [None]*q
for i in range(q):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    l1 = lca(x,K)
    l2 = lca(y,K)
#     print(x,y,l1,l2)
    ans[i] = (dist[x]+dist[K]-2*dist[l1]) + (dist[y]+dist[K]-2*dist[l2])
write("\n".join(map(str, ans)))