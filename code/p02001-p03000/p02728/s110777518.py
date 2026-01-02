import sys
input = sys.stdin.readline
sys.setrecursionlimit(500000)

from collections import deque

MOD = 10**9+7
INF = float('inf')

def inv(n): return pow(n, MOD-2, MOD)

kaijo_memo = []
def kaijo(n):
  if(len(kaijo_memo) > n): return kaijo_memo[n]
  if(len(kaijo_memo) == 0): kaijo_memo.append(1)
  while(len(kaijo_memo) <= n): kaijo_memo.append(kaijo_memo[-1] * len(kaijo_memo) % MOD)
  return kaijo_memo[n]

gyaku_kaijo_memo = []
def gyaku_kaijo(n):
  if(len(gyaku_kaijo_memo) > n): return gyaku_kaijo_memo[n]
  if(len(gyaku_kaijo_memo) == 0): gyaku_kaijo_memo.append(1)
  while(len(gyaku_kaijo_memo) <= n): gyaku_kaijo_memo.append(gyaku_kaijo_memo[-1] * pow(len(gyaku_kaijo_memo),MOD-2,MOD) % MOD)
  return gyaku_kaijo_memo[n]

def nCr(n,r):
  if n == r: return 1
  if n < r or r < 0: return 0
  ret = 1
  ret = ret * kaijo(n) % MOD
  ret = ret * gyaku_kaijo(r) % MOD
  ret = ret * gyaku_kaijo(n-r) % MOD
  return ret

N = int(input())
graph = [[] for i in range(N)]
for _ in range(N-1):
  a,b = list(map(int,input().split()))
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)
  
p = [-1 for i in range(N)] 
a = [[] for i in range(N)]

shori = []
def bfs(graph, start):
  N = len(graph)
  d = [INF] * N
  d[start] = 0
  q = deque([start])
  while q:
    u = q.popleft()
    shori.append(u)
    for v in graph[u]:
      if d[v] != INF: continue
      d[v] = d[u] + 1
      p[v] = u
      a[u].append(v)
      q.append(v)
  return d

bfs(graph,0)

size = [0 for i in range(N)]
def calc_size(x):
  if size[x]: return size[x]
  temp = 1
  for y in a[x]:
    temp += calc_size(y)
  size[x] = temp
  return size[x]
calc_size(0)

narabi = [0 for i in range(N)]
def calc_narabi(x):
  if narabi[x]: return narabi[x]
  temp = kaijo(size[x]-1)
  for y in a[x]:
    temp *= gyaku_kaijo(size[y])*calc_narabi(y)
    temp %= MOD
  narabi[x] = temp
  return narabi[x]
calc_narabi(0)

pnarabi = [1 for i in range(N)]
for i in shori[1:]:
  pnarabi[i] = narabi[p[i]] * inv(narabi[i]) * inv(nCr(size[p[i]]-1,size[i])) * pnarabi[p[i]] * nCr(N-1-size[i],N-size[p[i]])
  pnarabi[i] %= MOD

for i in shori[1:]:
  temp = narabi[i] * nCr(N-1,size[i]-1) *pnarabi[i]
  temp %= MOD
  narabi[i] = temp

print(*narabi,sep="\n")