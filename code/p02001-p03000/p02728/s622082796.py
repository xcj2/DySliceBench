import sys
sys.setrecursionlimit(10 ** 7)
class Tree:
  C, RL = {}, {}
  R, N, D, S, P, T = None, None, None, None, None, None
  TL = None
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
    s.S = {} #各ノードの子ノード
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
            if i not in s.S:
              s.S[i] = [j]
            else:
              s.S[i].append(j)
            s.P[j] = i
      s.D += 1
      F = Ft
  def dfs(s, x, y, r): #xからyまでの道O(M)
    if x == y:
      return [x]
    for i in s.C[x]:
      if i != r:
        t = s.dfs(i, y, x)
        if t != False:
          return [x] + t
    return False
  def dist(s, x): #最遠のノード,距離
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
  def tour(s): #オイラーツアー
    x = s.RL[1][0]
    s.T = [] #ツアー
    s.TL = [[] for _ in range(s.N)] #各ノードの出現位置
    s.TL[x].append(len(s.T))
    s.T.append(x)
    for i in (s.S[s.RL[1][0]]):
      s.tour_sub(i)
    return s.T
  def tour_sub(s, x): #オイラーツアーのサブ
    s.TL[x].append(len(s.T))
    s.T.append(x)
    if x in s.S:
      for i in (s.S[x]):
        s.tour_sub(i)
    s.TL[s.P[x]].append(len(s.T))
    s.T.append(s.P[x])
  def bottomUpDP(s):
    s.dp_init()
    for i in range(s.D - 1, 0, -1):
      T = s.RL[i]
      for j in T:
        s.dp_sub(j)
  def allDP(s):
    bDP = s.bottomUpDP()
    for i in range(2, s.D):
      T = s.RL[i]
      for j in T:
        s.dp_sub_exe_inv(j, s.P[j])
  def dp_init(s): #単位元で初期化
    s.DP = [1] * N
    s.sDP = [1] * N
  def dp_sub(s, x):
    if x not in s.S:
      return 0
    T = s.S[x]
    for i in T:
      s.dp_sub_exe(x, i)
  def dp_sub_exe(s, x, y): #ボトムアップの処理
    s.sDP[x] += s.sDP[y]
    s.DP[x] = s.DP[x] * s.DP[y] * com.com(s.sDP[x] - 1, s.sDP[y]) % MOD
  def dp_sub_exe_inv(s, x, y): #トップダウンの処理
    t = com.com(s.sDP[y] - 1, s.sDP[x]) * s.DP[x] % MOD
    t = s.DP[y] * s.inv(t, MOD)
    k = s.sDP[y] - s.sDP[x]
    k = com.com(s.sDP[y] - 1, k) % MOD
    s.sDP[x] = s.sDP[y]
    s.DP[x] = s.DP[x] * t * k % MOD
    return 
  def inv(s, a, mod): #逆元
    return pow(a, mod - 2, mod)
  
class comb():
  F = [1, 1]
  Fi = [1, 1]
  I = [0, 1]
  def __init__(self, num, mod):
    self.MOD = mod
    for i in range(2, num + 1):
      self.F.append((self.F[-1] * i) % mod)
      self.I.append(mod - self.I[mod % i] * (mod // i) % mod)
      self.Fi.append(self.Fi[-1] * self.I[i] % mod)
  def com(self, n, k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return self.F[n] * (self.Fi[k] * self.Fi[n - k] % self.MOD) % self.MOD

N = int(input())
ab = [list(map(int, input().split())) for _ in range(N - 1)]

MOD = 10 ** 9 + 7
com = comb(N, MOD)

T = Tree(N)
for a, b in ab:
  a -= 1
  b -= 1
  T.set(a, b)

T.makeRank(0)
T.allDP()

for i in T.DP:
  print(i)