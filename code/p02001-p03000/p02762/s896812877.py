import sys
sys.setrecursionlimit(10**6)

N, M, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(K)]

par = [n+1 for n in range(N)]
rank = [0 for _ in range(N)]
size = [1 for _ in range(N)]

# 木の根を求める
def find(x):
  if par[x-1] != x:
    par[x-1] = find(par[x-1])
  return par[x-1]
# x, y の属する集合を併合
def unite(x, y):
  rx = find(x)
  ry = find(y)
  if rx == ry:
    return
  if rank[rx-1] < rank[ry-1]:
    rx, ry = ry, rx
  par[ry-1] = rx
  size[rx-1] += size[ry-1]
  if rank[rx-1] == rank[ry-1]:
    rank[rx-1] += 1
# x, y が同じ集合に属するか否か
def same(x, y):
  return find(x) == find(y)
def getsize(x):
  return size[find(x)-1]

friends = [0 for _ in range(N)]
for A, B in AB:
  unite(A, B)
  friends[A-1] += 1
  friends[B-1] += 1

ans = [0 for _ in range(N)]

for n in range(N):
  ans[n] = getsize(n+1) - friends[n] -1

for C, D in CD:
  if same(C, D):
    ans[C-1] -= 1
    ans[D-1] -= 1
print(' '.join(map(str, ans)))