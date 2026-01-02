MOD = 10 ** 9 + 7
def add(a, b):
  return (a + b) % MOD
def sub(a, b):
  return (a - b) % MOD
def mul(a, b):
  return ((a % MOD) * (b % MOD)) % MOD
def div(a, b):
  return ( (a % MOD) * (power(b, MOD)) ) % MOD
def power(a, b):
  return pow(a, b, MOD)

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
  
N = 2000
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % MOD )
    inverse.append( ( -inverse[MOD % i] * (MOD//i) ) % MOD )
    g2.append( (g2[-1] * inverse[-1]) % MOD )

n, k = map(int, input().split())
for i in range(1, k+1):
  cnt = mul(cmb(n-k+1, i, MOD), cmb(k-1, i-1, MOD))
  print(cnt)
