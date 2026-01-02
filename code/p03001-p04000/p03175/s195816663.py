N = int(input())
xy = [list(map(int, input().split())) for i in range(N - 1)]

MOD = 10 ** 9 + 7

class Tree:
  C, RL = {}, {}
  R, N, D = None, None, None
  def __init__(s, num):
    s.N = num
  def setC(s, a, b):
    if a in s.C: s.C[a].append(b)
    else: s.C[a] = [b]
    if b in s.C: s.C[b].append(a)
    else: s.C[b] = [a]
  def makeRank(s, root = 0):
    s.R = [0] * s.N
    s.R[root] = 1
    s.RL[1] = [root]
    F = [root]
    s.D = 2
    while F != []:
      Ft = []
      s.RL[s.D] = []
      for i in F:
        for j in s.C[i]:
          if s.R[j] == 0:
            s.R[j] = s.D
            Ft.append(j)
            s.RL[s.D].append(j)
      s.D += 1
      F = Ft
  def nasu(s, x = 0):
    DP = [[1] * 2 for _ in range(s.N)]
    for d in range(s.D - 2, 0, -1):
      for i in s.RL[d]:
        L = []
        for j in s.C[i]:
          if s.R[j] > s.R[i]:
            L.append(j)
        b = 1
        w = 1
        for k in L:
          b = b * DP[k][0] % MOD
          w = w * (DP[k][0] + DP[k][1]) % MOD
        DP[i] = [w, b]
    return (DP[x][0] + DP[x][1]) % MOD

T = Tree(N)
if N == 1:
  print(2)
  exit()
for x, y in xy:
  x -= 1
  y -= 1
  T.setC(x, y)

T.makeRank()

print(T.nasu())