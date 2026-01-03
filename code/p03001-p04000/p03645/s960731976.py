import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
query = [[] for _ in range(N)]
for _ in range(M):
    a, b = mapint()
    query[a-1].append(b-1)
    query[b-1].append(a-1)

checked = [0]*N
ans = False
def dfs(now, cnt):
    global ans
    if cnt==2:
        if now==N-1:
            ans = True
        return
    checked[now] = 1
    for nx in query[now]:
        if not checked[nx]:
            dfs(nx, cnt+1)

dfs(0, 0)
if ans:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')