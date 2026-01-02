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
xy = []

ins = [0]*n
graph = [[] for _ in range(n)]

dp = [0]*n
for _ in range(m):
    x,y = li_()
    ins[y] += 1
    graph[x].append(y)
    
stack = []
for i in range(n):
    if ins[i] == 0:
        stack.append(i)

while stack:
    nex_stack = []
    for point in stack:
        for nexp in graph[point]:
            dp[nexp] = max(dp[nexp], dp[point]+1)
            ins[nexp] -= 1
            if ins[nexp] == 0:
                nex_stack.append(nexp)
                
    stack = nex_stack
    
print(max(dp))
            