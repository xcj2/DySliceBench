import math
import sys
K, N = [int(i) for i in input().split(' ')]
mod = 998244353
sys.setrecursionlimit(100000)

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def cmb_f(n, r, mod):
#    print(n, r)
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
#    print(g1[n] * g2[r] * g2[n-r] % mod)
    return g1[n] * g2[r] * g2[n-r] % mod

NNN = 10**4
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range( 2, NNN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

def EN(i):
    k2 = int((K - abs(K - int((i-1)/2) * 2) )/2)
    k1 = K - k2*2 - (1 if i % 2 == 0 else 0)
    result = 0
    for j in range(k2+1):
        if N < j:
            break
        result = (result + mul(mul(cmb_f(k2, j, mod) , cmb_f(N+k1-1, j+k1-1, mod)) , pow(2, j) % mod))% mod
    if i % 2 == 1:
        return result
    for j in range(k2+1):
        if N-1 < j:
            break
        result = (result + mul(mul(cmb_f(k2, j, mod), cmb_f(N+k1-2, j+k1-1, mod)), pow(2, j) % mod))% mod
    return result

if K == 1:
    print(0)
else:
    result = []
    for i in range(K):
        result.append(str(EN(i+2)))
    print("\n".join(result + result[:-1][::-1]))
