def main(N, a):

  from queue import Queue as Que

  put = Que.put
  get = Que.get
  emp = Que.empty
  class Tree:
    def __init__(s, N):
      s.N = N
      s.R = {}
    def add(s, a, b):
      if a not in s.R: s.R[a] = [b]
      else: s.R[a].append(b)
    def makeTree(s, root):
      S = Que()
      s.D = [0] * s.N
      put(S, root)
      while not emp(S):
        t = get(S)
        if t not in s.R: continue
        for i in s.R[t]:
          s.D[i] = s.D[t] + 1
          put(S, i)
      s.M = max(s.D) + 1
      s.DL = [[] for _ in range(s.M)]
      for i in range(s.N):
        s.DL[s.D[i]].append(i)
    def sun(s, x):
      if x not in s.R: return []
      else: return s.R[x]

  T = Tree(N)

  for i in range(N - 1):
    T.add(a[i] - 1, i + 1)

  T.makeTree(0)

  D = T.D
  DL = T.DL
  M = T.M
  MEMO = [1] * N

  for i in range(M - 1, -1, -1):
    for n in T.DL[i]:
      R = {}
      L = []
      for s in T.sun(n):
        k = MEMO[s]
        if k in R:
          R[k] += 1
        else:
          R[k] = 1
          L.append(k)
      L.sort()
      mox = 0
      for i in range(len(L)):
        if mox > L[i]:
          mox += R[L[i]]
        else:
          mox = L[i] + R[L[i]]
        
      MEMO[n] = mox

  ans = MEMO[0]
  print(ans)

N = int(input())
a = [int(input()) for _ in range(N - 1)]

main(N, a)

"""
import random
for i in range(10):
  N = random.randrange(4) + 4
  a = [0] * (N - 1)
  L = [0]
  D = [i for i in range(N)]
  for j in range(N - 1):
    if a[j] != 0: continue
    k = L[random.randrange(len(L))]
    n = j + 1
    while n != 0:
      D.remove(n)
      L.append(n)
      a[n - 1] = k + 1
      k = n
      n = D[random.randrange(len(D))]
  print("N", N)
  print("n", [i for i in range(2, N + 1)])
  print("a", a)
  main(N, a)
"""