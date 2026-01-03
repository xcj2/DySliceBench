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
    ansn_1 = neg
    ans_n = neg
    
    for i in range(n+1):
        for frm, node in enumerate(graph):
            for cost, to in node:
                dist[to] = max(dist[to], dist[frm] + cost)
        
        if i == n-1:
            ansn_1 = dist[-1]
        elif i == n:
            ans_n = dist[-1]
            
    if ansn_1 != ans_n:
        return "inf"
    else:
        return ans_n
        

n,m = li()

graph = [[] for _ in range(n)]
for i in range(m):
    a,b,c = li()
    a -= 1
    b -= 1
    graph[a].append((c,b))
    
ans = bf(graph)
print(ans)