###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###
import time

# 拡張ユークリッド互除法
# ax + by = gcd(a,b)の最小整数解を返す
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# mを法とするaの乗法的逆元
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

N, A, B, C = mi()

MOD = 10**9+7
a = (A * modinv(A+B, MOD)) % MOD
b = (B * modinv(A+B, MOD)) % MOD
gyakugenofAB = (100 * modinv(A+B, MOD)) % MOD

# 累乗を返すリスト
#[0]行にはaの階乗を、[1]行にはbの階乗を入れる
powlist = [[-1] * (N+1) for _ in range(2)]
preA = 1
preB = 1
powlist[0][0] = 1
powlist[1][0] = 1
for i in range(1,N+1):
  preA = (preA * a) % MOD
  preB = (preB * b) % MOD
  powlist[0][i] = preA
  powlist[1][i] = preB


#cmb(m)でmCn-1を計算
import math
Nmin1fct = modinv(math.factorial(N-1),MOD) % MOD

#一度でも計算したらflagがオン
flag = 0
preans = 1
def cmb(k):
  global flag
  global preans
  ans = 1
  if flag == 0:
    flag = 1
    for i in range(max(1,k-1),k-N,-1):
      ans = (ans * i) % MOD
    preans = (ans * Nmin1fct) % MOD
    return preans
  else:
    preans = (preans * (k-1) * modinv(max(1, k-N),MOD)) % MOD
  return preans
#cmbの計算終わり


#期待値（確率×回数）を足し上げていく。
#N回目～2N-1回目についてループを回す
#m-1Cn-1なことに注意
e = 0
cnt = 0
for m in range(N, 2*N):
#  cnt += 1
#  if cnt % 1000 == 0: print(cnt)
#  start_time = time.perf_counter()
  e += (m * gyakugenofAB * (cmb(m) % MOD) * ((powlist[0][N] * powlist[1][m-N]) + (powlist[0][m-N] * powlist[1][N])))
  e %= MOD
#  print(time.perf_counter() - start_time)


print(e)
