import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n,m = li()

graph = [[] for _ in range(n)]
for _ in range(m):
    l,r,d = li()
    l -= 1
    r -= 1
    graph[l].append((d,r))
    graph[r].append((-d,l))
    
searched = [False]*n
dist = [float("inf") for _ in range(n)]

exist = True
for i in range(n):
    if not searched[i]:
        dist[i] = 0
        searched[i] = True
        stack = [(0,i)]
        
        while stack:
            cost, cur = stack.pop()
            for nex_cost, nex_node in graph[cur]:
                if searched[nex_node]:
                    if cost + nex_cost != dist[nex_node]:
                        exist = False
                        
                else:
                    stack.append((cost+nex_cost, nex_node))
                    dist[nex_node] = cost + nex_cost
                    searched[nex_node] = True
                    
if exist:
    print("Yes")
else:
    print("No")