import sys,os,io
input = sys.stdin.readline
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

N = int(input())
edge = [[] for _ in range(N)]
for i in range(N-1):
  a,b = list(map(int, input().split()))
  edge[a-1].append(b-1)
  edge[b-1].append(a-1)
mod = 10**9+7

def fact(N):
  ans = [1]*(N+1)
  for i in range(1,N+1):
    ans[i] = ans[i-1]*i%mod
  return ans

def combs_mod(n,k):
  #nC0からnCkまで
  inv = [1]*(k+1)
  for i in range(1,k+1):
    inv[i] = pow(i,mod-2,mod)
  ans = [1]*(k+1)
  for i in range(1,k+1):
    ans[i] = ans[i-1]*(n+1-i)*inv[i]%mod
  return ans

def dfs(start):
  stack = [start]
  parent = [N]*N
  parent[start] = -1
  fac = fact(N)
  while stack:
    v = stack[-1]
    marker = 0
    for u in edge[v]:
      if u==parent[v]:
        continue
      if parent[u]==N: #子へ降ろす
        marker = 1
        parent[u] = v
        stack.append(u)
      else: #子から吸い上げる
        part_num[v] += part_num[u]
        ans[v] *= pow(fac[part_num[u]],mod-2,mod)*ans[u]%mod
        ans[v] %= mod
    if marker==0:
      stack.pop()
      ans[v] *= fac[part_num[v]-1]
      ans[v] %= mod
  return

def dfs2(start):
  stack = [start]
  parent = [N]*N
  parent[start] = -1
  p_value = [0]*N
  combs = combs_mod(N-1,N-1)
  while stack:
    v = stack.pop()
    for i,u in enumerate(edge[v]):
      if u==parent[v]:
        continue
      parent[u]=v
      p_value[u] = ans[v]*pow(ans[u]*combs[part_num[u]],mod-2,mod)%mod
      ans[u] *= combs[part_num[u]-1]*p_value[u]
      ans[u] %= mod
      stack.append(u)
  return

ans = [1]*N
part_num = [1]*N
dfs(0)
dfs2(0)
print(*ans, sep='\n')