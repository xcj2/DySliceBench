import sys
mod = pow(10, 9) + 7

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def cmb(n, r):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
def H(n, r):
    return cmb(n+r-1, r-1) 

NNN = (10**5)
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range( 2, NNN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

N, K = map(int, input().split())
for L in range(1, K+1):
    print(H(K - L, L)*H((N-K) - (L-1), L+1)%mod)
