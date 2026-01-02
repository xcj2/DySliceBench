"""負辺ありの有向グラフの最短経路問題、ベルマンフォード法"""
import sys
sys.setrecursionlimit(10**6)

n,m,p = map(int, input().split())

INF = 1001001001

to = [[] for _ in range(2505)]
rto = [[] for _ in range(2505)]
reachableFrom1 = [False for _ in range(2505)]
reachableToN = [False for _ in range(2505)]
ok = [False for _ in range(2505)]

def dfs(v):
    """1から到達できる頂点の列挙"""
    if reachableFrom1[v]: return
    reachableFrom1[v] = True
    for u in to[v]:
        dfs(u)

def rdfs(v):
    """Nに到達できる頂点の列挙"""
    if reachableToN[v]: return
    reachableToN[v] = True
    for u in rto[v]:
        rdfs(u)

edges = []
for i in range(m):
    a,b,c = map(int, input().split())
    a -= 1; b -= 1
    c -= p
    c = -c
    edges.append((a,b,c))
    to[a].append(b) # 到達可能性を判定するための変数
    rto[b].append(a) # nに辿り着けるかを判定するための変数
    
dfs(0)
rdfs(n-1)
for i in range(n):
    ok[i] = reachableFrom1[i] & reachableToN[i] # okになっている頂点だけを考える
# ベルマンフォード
def main():
    global edges, ok
    d = [INF for _ in range(n)]
    d[0] = 0
    upd = True
    step = 0 # 負閉路検出用。更新回数がnステップを超えたら負閉路あり
    while upd:
        upd = False
        for i in range(m):
            a,b,c = edges[i]
            if not ok[a]: continue
            if not ok[b]: continue
            newD = d[a]+c
            if newD < d[b]:
                upd = True
                d[b] = newD
        step += 1
        if step > n:
            print(-1)
            return
    ans = -d[n-1]
    ans = max(ans,0)
    print(ans)
    return
    
main()