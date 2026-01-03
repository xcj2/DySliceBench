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

# 隣接リストを作成(key:b, val:a)
edges = []
for _ in range(m):
    ai, bi, ci = li()
    ai -= 1
    bi -= 1
    edges.append((ai, bi, ci))

# ベルマンフォード
dist = [[-10**18]*n for _ in range(2*n+3)]
for i in range(2*n+2):
    dist[i][0] = 0

ans = -10**18
chk = -10**18

for i in range(2*n+2):
    for ai, bi, ci in edges:
        dist[i+1][bi] = max(dist[i+1][bi],
                            dist[i][bi],
                            dist[i][ai] + ci)
    if i == n:
        ans = dist[i][n-1]
        
    elif i == 2*n+1:
        chk = dist[i][n-1]
        
print(ans if ans >= chk else "inf")