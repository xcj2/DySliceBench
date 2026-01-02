import sys
sys.setrecursionlimit(1000000)

def make_adlist(n):
  adlist = [[] for _ in range(n)]
  for _ in range(n-1):
    a, b = map(lambda x:int(x)-1, input().split())
    adlist[a] += [b] 
    adlist[b] += [a]
  return adlist

def dfs(adlist, s, dist, d):
  for nxt in adlist[s]:
    if dist[nxt] == -1:
      dist[nxt] = d
      dfs(adlist, nxt, dist, d+1)

def main():
  n, u, v = map(int, input().split())
  u -= 1
  v -= 1
  adlist = make_adlist(n)
  t_dist = [-1]*n
  t_dist[u] = 0
  dfs(adlist, u, t_dist, 1)
  a_dist = [-1]*n
  a_dist[v] = 0
  dfs(adlist, v, a_dist, 1)
  ans = 0 
  for i in range(n):
    if t_dist[i] < a_dist[i]:
      ans = max(ans, a_dist[i]-1)
  print(ans)

if __name__ == "__main__":
  main()