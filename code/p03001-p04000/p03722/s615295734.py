# 入力
import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())


def bf(graph: list):
    neg = -10**16
    n = len(graph)
    dist = [neg]*n
    dist[0] = 0
    
    hasUpdate = True
    cnt = 0
    cur = neg
    while hasUpdate:
        hasUpdate = False
        cnt += 1
        
        for frm, node in enumerate(graph):
            for cost, to in node:
                bef = dist[to]
                dist[to] = max(dist[to], dist[frm] + cost)
                
                # 更新されたならupdateをTrueに
                if dist[to] != bef:
                    hasUpdate = True
        
        if cnt == n:
            cur = dist[-1]
            
        if cnt == n+1:
            if dist[-1] == cur:
                return dist[-1]
            else:
                return "inf"
        
    return dist[-1]
                

n,m = li()

graph = [[] for _ in range(n)]
for i in range(m):
    a,b,c = li()
    a -= 1
    b -= 1
    graph[a].append((c,b))
    
ans = bf(graph)
print(ans)