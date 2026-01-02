import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
'''
from collections import deque
N, Q = mi()
D = li2(N-1)
px = li2(Q)
que = deque()

adj = [[] for i in range(N+1)]

for i in range(N-1):
    adj[D[i][0]].append(D[i][1])

ans = [0]*(N+1)
for j in range(Q):
    ind, a = px[j][0], px[j][1]
    que.append(ind)
    while(que!=deque()):
        v = que.popleft()
        ans[v] += a
        for e in adj[v]:
            que.append(e)


for i in range(1, N+1):
    print(ans[i], ' ', end='')
'''

from collections import deque
sys.setrecursionlimit(10**9)

#入力受け取り
N, Q = mi()
x = li2(N-1)
#p = li2(Q)

cnt = [0]*N
for i in range(Q):
    p0, p1 = mi()
    cnt[p0-1] += p1

#隣接リスト作成
adj = [[] for i in range(N)]
for i in range(N-1):
    x[i][0] -= 1
    x[i][1] -= 1
    adj[x[i][0]].append(x[i][1])
    adj[x[i][1]].append(x[i][0])

que = deque()
ans = [0]*N

#for a in range(N):
que.append((0, 0))
num = 0
while que!=deque():
    v = que.popleft()
    ans[v[1]] = ans[v[0]] + cnt[v[1]]
    for next in adj[v[1]]:
        if next != v[0]:
            que.append((v[1], next))

for k in ans:
    print(k, '', end='')