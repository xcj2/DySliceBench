from collections import deque
def bfs(n,e,fordfs):
    #点の数、スタートの点、有向グラフ
    W = [-1]*n
    W[e] = 0
    que = deque()
    que.append(e)
    len = [0]*n
    color = [0]*n
    while que:
        now = que.popleft()
        nowv = W[now]
        nowlen = len[now]
        nowcolor = color[now]
        for ne in fordfs[now]:
            if nowv == W[ne]:
                return -1
            elif W[ne] == -1:
                W[ne] = (nowv+1) % 2
                len[ne] = nowlen+1
                if nowcolor==0:
                    color[ne] = 1
                que.append(ne)
    return color[:n//2]
#############################################################
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')
ans = []

N = I()
uvw = [LI() for _ in range(N-1)]
g = [[] for i in range(2*N)]

for i in range(N-1):
    x = uvw[i][0] - 1
    y = uvw[i][1] - 1
    if uvw[i][2]%2==1:
        g[x].append(y)
        g[y].append(x)
    else:
        g[x].append(N+x)
        g[N+x].append(y)
        g[y].append(N+y)
        g[N+y].append(x)

ans = bfs(2*N,0,g)

for i in ans:
    print(i)
