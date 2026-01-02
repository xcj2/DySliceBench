import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist
  return list(map(int,input().split()))
def m(): #複数文字
  return map(int,input().split())
def onem(): #Nとかの取得
  return int(input())
def s(x): #圧縮
  a = []
  if len(x) == 0:
    return []
  aa = x[0]
  su = 1
  for i in range(len(x)-1):
    if aa != x[i+1]:
      a.append([aa,su])
      aa = x[i+1]
      su = 1
    else:
      su += 1
  a.append([aa,su])
  return a
def jo(x): #listをスペースごとに分ける
  return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
  return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False

def pow_k(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

"""
def nibu(x,n,r):
  ll = 0
  rr = r
  while True:
    mid = (ll+rr)//2

  if rr == mid:
    return ll
  if (ここに評価入れる):
    rr = mid
  else:
    ll = mid+1
"""

mod = 10**9+7 #出力の制限
N = 10**6 * 2 + 2
def cmb(n, r):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
def p(n,r):
    if ( r<0 or r>n ):
        return 0
    return g1[n] * g2[n-r] % mod

g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
# a = cmb(n,r)

r1,c1,r2,c2= m()

p1 = 0

p2 = 0

p3 = 0

p4 = 0

for i in range(1,r2+2):
  p1 += cmb(c2+i,i)
  p1 %= mod
for i in range(1,r1+1):
  p2 += cmb(c2+i,i)
  p2 %= mod
for i in range(1,r2+2):
  p3 += cmb(c1+i-1,i)
  p3 %= mod
for i in range(1,r1+1):
  p4 += cmb(c1+i-1,i)
  p4 %= mod

print((p1-p2-p3+p4)%mod)




