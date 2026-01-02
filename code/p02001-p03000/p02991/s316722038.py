from collections import deque
def bfs(n,e,fordfs):
    #点の数、スタートの点、有向グラフ
    W = [-1]*n
    W[e] = 0
    que = deque()
    que.append(e)
    len = [0]*n
    while que:
        now = que.popleft()
        nowv = W[now]
        nowlen = len[now]
        for ne in fordfs[now]:
            if W[ne] == -1:
                W[ne] = nowv+1
                len[ne] = nowlen+1
                que.append(ne)
    return W
#############################################################

import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')
ans = int(0)

N, M = LI()
V = [[] for i in range(3*N)]
#print(V)
for i in range(M):
    u, v = LI()
    V[u-1].append(N+v-1)
    V[N+u-1].append(2*N+v-1)
    V[2*N+u-1].append(v-1)
cou = []
S, T = LI()
#print(V)

cou = bfs(3*N, S-1, V)
#print(cou)
ans = cou[T-1]//3
print(ans)
