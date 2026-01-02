import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

from collections import defaultdict
from collections import deque
import heapq

MOD = 998244353

def DD(arg): return defaultdict(arg)

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

class NTT_convolution:
  def __init__(self, ROOT=3, MOD=998244353):
    self.ROOT = 3
    self.MOD = 998244353
    self.roots  = [pow(self.ROOT,(self.MOD-1)>>i,self.MOD) for i in range(24)] # 1 の 2^i 乗根
    self.iroots = [pow(x,self.MOD-2,self.MOD) for x in self.roots] # 1 の 2^i 乗根の逆元
 
  def untt(self,a,n):
    for i in range(n):
      m = 1<<(n-i-1)
      for s in range(1<<i):
        w_N = 1
        s *= m*2
        for p in range(m):
          a[s+p], a[s+p+m] = (a[s+p]+a[s+p+m])%self.MOD, (a[s+p]-a[s+p+m])*w_N%self.MOD
          w_N = w_N*self.roots[n-i]%self.MOD
 
  def iuntt(self,a,n):
    for i in range(n):
      m = 1<<i
      for s in range(1<<(n-i-1)):
        w_N = 1
        s *= m*2
        for p in range(m):
          a[s+p], a[s+p+m] = (a[s+p]+a[s+p+m]*w_N)%self.MOD, (a[s+p]-a[s+p+m]*w_N)%self.MOD
          w_N = w_N*self.iroots[i+1]%self.MOD
      
    inv = pow((self.MOD+1)//2,n,self.MOD)
    for i in range(1<<n):
      a[i] = a[i]*inv%self.MOD
 
  def convolution(self,a,b):
    la = len(a)
    lb = len(b)
    deg = la+lb-2
    n = deg.bit_length()
    if min(la, lb) <= 50:
      if la < lb:
        la,lb = lb,la
        a,b = b,a
      res = [0]*(la+lb-1)
      for i in range(la):
        for j in range(lb):
          res[i+j] += a[i]*b[j]
          res[i+j] %= self.MOD
      return res
 
    N = 1<<n
    a += [0]*(N-len(a))
    b += [0]*(N-len(b))
    self.untt(a,n)
    self.untt(b,n)
    for i in range(N):
      a[i] = a[i]*b[i]%self.MOD
    self.iuntt(a,n)
    return a[:deg+1]

N = int(input())
NTT = NTT_convolution()

nokori = [1]
for n in range(1,2*N+10):
  nokori.append((nokori[-1]*(2*n-1)*(2*n)*inv(2)*inv(n))%MOD)

dic = DD(int)
for _ in range(N*2):
  dic[int(input())] += 1
A = [dic[k] for k in dic]
  
P = []
for a in A:
  temp = 1
  count = 0
  P.append([temp])
  while a >= 2:
    temp *= a*(a-1)//2
    temp %= MOD
    count += 1
    P[-1].append((temp*gyaku_kaijo(count))%MOD)
    a -= 2

Q = []
for i in range(len(P)):
  heapq.heappush(Q,(len(P[i]),i))

while len(Q)>1:
  _,p = heapq.heappop(Q)
  _,q = heapq.heappop(Q)
  temp = NTT.convolution(P[p], P[q])
  P.append(temp)
  heapq.heappush(Q,(len(temp),len(P)-1))
Q = list(P[-1])

ans = 0
M = len(Q)

def sign(x):
  if x%2: return -1
  else: return 1

for i in range(M):
  ans += sign(i) * Q[i] * nokori[N-i]
  ans %= MOD
  
print(ans)