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
    s.D = 1
    while s.RL[s.D] != []:
      s.D += 1
      s.RL[s.D] = []
      for i in s.RL[s.D - 1]:
        for j in s.C[i]:
          if s.R[j] == 0:
            s.R[j] = s.D
            s.RL[s.D].append(j)
            if i not in s.S: s.S[i] = [j]
            else: s.S[i].append(j)
            s.P[j] = i      
  def bottomUpDP(s):
    for i in range(s.D - 2, 0, -1):
      T = s.RL[i]
      for j in T:
        if j not in s.S: continue
        for k in s.S[j]:
          s.dp_sub_exe(j, k)
  def topDownDP(s):
    for i in range(2, s.D):
      T = s.RL[i]
      for j in T:
        s.dp_sub_exe_inv(j, s.P[j])
  def allDP(s):
    s.dp_init()
    s.bottomUpDP()
    s.topDownDP()
    return s.DP
  def dp_init(s): #単位元で初期化
    s.DP = [1] * N
    s.sDP = [1] * N
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
DP = T.allDP()

for i in DP:
  print(i)