#################################
##ワーシャルフロイド法 n~3
#################################
def warshall_floyd(n,d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
##############################
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')
ans = int(0)
N,M,L =LI()
s = []
t = []
dp = [[inf] * (N) for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    dp[a-1][b-1] = c
    dp[b-1][a-1] = c
Q = I()
for i in range(Q):
    a,b = LI()
    s.append(a-1)
    t.append(b-1)

for i in range(N):
    dp[i][i] = 0

#print(warshall_floyd(N,dp))
d1 = [[0] * (N) for _ in range(N)]
d1 = warshall_floyd(N,dp)

newdp = [[inf] * (N) for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if d1[i][j]<=L:
            newdp[i][j] = 1
            newdp[j][i] = 1

for i in range(N):
    newdp[i][i] = 0
#print(newdp)
#print(warshall_floyd(N,newdp))
d2 = [[0] * (N) for _ in range(N)]
d2 = warshall_floyd(N,newdp)

for i in range(Q):
    ans = d2[s[i]][t[i]]-1
    if ans!= inf:
        print(ans)
    else:
        print("-1")
