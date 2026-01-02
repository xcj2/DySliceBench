from sys import exit, setrecursionlimit
setrecursionlimit(1000000)

def dfs(v, dp, to):
  t = dp[v]
  if t >= 0:
    return t
  dp[v] = 0
  t = 0
  for u in to[v]:
    res = dfs(u, dp, to)
    if res == 0:
      print('-1')
      exit()
    if res > t:
      t = res
  t += 1
  dp[v] = t
  return t

def toId(i, j, id_db):
  if i < j:
    return id_db[i][j]
  else:
    return id_db[j][i]

def main():
  N = int(input())
  a = [[int(e) - 1 for e in input().split()] for _ in range(N)]

  id_db = [[0] * N for _ in range(N)]

  dp = [-1] * (N * (N - 1) // 2)
  to = [[] for _ in range(N * (N - 1) // 2)]

  v = 0
  for i in range(N):
    for j in range(i + 1, N):
      id_db[i][j] = v
      v += 1

  for i in range(N):
    for j in range(N - 1):
      a[i][j] = toId(i, a[i][j], id_db)
    for j in range(N - 2):
      to[a[i][j]].append(a[i][j + 1])

  print(max(dfs(i, dp, to) for i in range(N * (N - 1) // 2)))

main()
