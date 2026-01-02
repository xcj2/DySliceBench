class Tree:
  C, RL = {}, {}
  R, N, D, S, P = None, None, None, None, None
  SN = None
  def __init__(s, num):
    s.N = num
  def set(s, a, b):
    if a in s.C: s.C[a].append(b)
    else: s.C[a] = [b]
    if b in s.C: s.C[b].append(a)
    else: s.C[b] = [a]
  def makeRank(s, root):
    s.R = [0] * s.N #各ノードのランク
    s.R[root] = 1
    s.RL[1] = [root] #各ランクのノード
    s.S = [[] for _ in range(s.N)] #各ノードの子ノード
    s.P = [-1] * s.N #各ノードの親ノード
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
            s.S[i].append(j)
            s.P[j] = i
      s.D += 1
      F = Ft
  def dfs(s, x): #最遠のノード,距離
    t = [-1] * s.N
    S = [x]
    ans = x
    ansn = 0
    t[x] = 0
    while S != []:
      k = S.pop()
      for i in s.C[k]:
        if t[i] == -1:
          t[i] = t[k] + 1
          S.append(i)
          if t[i] > ansn:
            ansn = t[i]
            ans = i
    return ans, ansn
  def getDi(s, x = 0): #直径
    a, _ = s.dfs(x)
    b, ans = s.dfs(a)
    return ans
  def getDeep(s, x): #xの子孫のうち一番深い深さ
    ans = 0
    if x in s.S:
      for i in s.S[x]:
        ans = max(ans, s.getDeep(i))
      return ans + 1
    else:
      return 0
  def getParent(s, x, n): #xのn世代前の親
    if n == 0:
      return x
    if s.P[x] == -1:
      return -n
    return s.getParent(s.P[x], n - 1)
  def countSon(s):
    s.SN = [0] * s.N
    for i in range(s.D - 1, 0, -1):
      for j in s.RL[i]:
        cnt = 1
        for k in s.S[j]:
          cnt += s.SN[k]
        s.SN[j] = cnt

class powmod():
  F = [1, 2]
  Fi = [1, 2]
  I = [0, 1]
  def __init__(self, num, mod):
    self.MOD = mod
    k = 2
    for i in range(2, num + 1):
      self.F.append((self.F[-1] * k) % mod)
      self.I.append(mod - self.I[mod % k] * (mod // k) % mod)
      self.Fi.append(self.Fi[-1] * self.I[k] % mod)

class Inv:
  def __init__(s, mod):
    s.MOD = mod
  def modpow(s, a, n):
    res = 1
    while n > 0:
      if n & 1:
        res = res * a % s.MOD
      a = a * a % s.MOD
      n >>= 1
    return res
  def invx(s, a):
    return s.modpow(a, s.MOD - 2)
  def invL(s, a, n):
    ia = s.invx(a)
    L = [1] * (n + 1)
    for i in range(1, n + 1):
      L[i] = L[i - 1] * ia % s.MOD
    return L


N = int(input())
AB = [list(map(int, input().split())) for _ in range(N - 1)]

T = Tree(N)
L = [0] * N
for a, b in AB:
  T.set(a - 1, b - 1)
  L[a - 1] += 1
  L[b - 1] += 1

for i in range(N):
  if L[i] == 1:
    root = i

T.makeRank(root)
T.countSon()

MOD = 10 ** 9 + 7
ans = 0


PM = powmod(N, MOD)
I = Inv(MOD)
y = I.invx(PM.F[N])

ans = 0
for i in range(N):
  if i == root: continue
  if T.S[i] == []: continue
  L = []
  cnt = 0
  for j in T.S[i]:
    L.append(T.SN[j])
    cnt += T.SN[j]
  L.append(N - cnt - 1)

  t = PM.F[N - 1] - 1
  for j in L:
    t = t - PM.F[j] + 1
    if t < 0:
      t += MOD
  ans = (ans + t * y) % MOD

print(ans)


