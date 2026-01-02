def inpl(): return list(map(int, input().split()))
N, K = inpl()
R = N-K

MOD = 10**9 + 7
def cmb(n, r, mod=MOD):
    if ( r<0 or r>n ):
        return 0
    
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


size = 10000
g1, g2, inverse = [0]*size, [0]*size, [0]*size
 
g1[:2] = [1, 1] # 元テーブル
g2[:2] = [1, 1] #逆元テーブル
inverse[:2] = [0, 1] #逆元テーブル計算用テーブル
 
for i in range(2, size):
    g1[i] =  ( g1[i-1] * i ) % MOD 
    inverse[i] = (-inverse[MOD % i] * (MOD//i) ) % MOD 
    g2[i] =  (g2[i-1] * inverse[i]) % MOD

def calc(i, x):
    if R - (i-1) - x < 0:
        return 0
    else:
        a = R-x-(i-1)
        b = i-1+x-1
        return cmb(K-1, i-1) * cmb(a+b, a)

for i in range(1, K+1):
    b = R - (i - 1)
    print(cmb(K-1, i-1)*cmb(b+i, b)%MOD)
