import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n = ni()
red = []
blue = []

for _ in range(n):
    red.append(list(li()))
    
for _ in range(n):
    blue.append(list(li()))
    
# 二部グラフの作成
graph = [{} for _ in range(2*n+2)]

for i,r in enumerate(red):
    for j,b in enumerate(blue):
        if r[0]<b[0] and r[1]<b[1]:
            graph[i+1].update({n+j+1: [1, 1]})
            graph[n+j+1].update({i+1: [0, 0]})
            
for i in range(1,n+1):
    graph[0].update({i: [1, 1]})
    graph[i].update({0: [0, 0]})
    
    graph[n+i].update({2*n+1: [1, 1]})
    graph[2*n+1].update({n+i: [0, 0]})
    

# 最大フロー
def dfs(start:int, goal:int, flow:int, visited:list):
    if start == goal:
        return flow
    
    visited[start] = True
    
    for key,value in graph[start].items():
        to = key
        cap, isFwd = value
        
        if not visited[to] and cap > 0:
            d = dfs(to, goal, min(flow, cap),visited)
            
            if d > 0:
                graph[start][to][0] -= d
                graph[to][start][0] += d
                
                return d
            
    return 0

def max_flow(start: int, goal: int):
    INF = float("inf")
    flow = 0
    while True:
        visited = [False]*(2*n+2)
        f = dfs(start,goal,INF,visited)
        
        if f == 0:
            return flow
        flow += f
        
ans = max_flow(0,2*n+1)
print(ans)