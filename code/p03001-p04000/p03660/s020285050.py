import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
query = [[] for _ in range(N)]
ab = []
for _ in range(N-1):
    a, b = mapint()
    query[a-1].append(b-1)
    query[b-1].append(a-1)
    ab.append((a-1, b-1))

def dfs_lis(start):
    checked = [0]*N
    dist = [0]*N
    def dfs(now):
        checked[now] = 1
        for nx in query[now]:
            if not checked[nx]:
                dist[nx] = dist[now]+1
                dfs(nx)
    dfs(start)
    return dist

fe = dfs_lis(0)
snu = dfs_lis(N-1)
cnt = 0
for f, s in zip(fe, snu):
    if f<=s:
        cnt += 1

if cnt>N//2:
    print('Fennec')
else:
    print('Snuke')