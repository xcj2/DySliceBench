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

n,m = li()

# graph
adj_list = [[] for _ in range(n)]

for _ in range(m):
    a,b,c = li()
    a -= 1
    b -= 1
    adj_list[a].append((c,b))

# bellman-ford
INF = -10**15
dist = [INF]*n
dist[0] = 0
for j in range(n+1):
    for i in range(n):
        updated = False
        for cost, nex in adj_list[i]:
            bef = dist[nex]
            dist[nex] = max(dist[nex], dist[i]+cost)
            if bef != dist[nex]:
                updated = True
        
    if j == n-1:
        dis_j1 = dist[n-1]
        
    if j == n:
        dis_j = dist[n-1]
        
if dis_j1 != dis_j:
    print("inf")
else:
    print(dis_j)