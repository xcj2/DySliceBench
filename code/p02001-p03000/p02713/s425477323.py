import sys
mod = pow(10, 9) + 7
sys.setrecursionlimit(pow(10, 8))

def power(x, y):
    if   y == 0: return 1
    elif y == 1	 : return x % mod
    elif y % 2 == 0 : return power(x, y//2)**2 % mod
    else: return power(x, (y-1)//2)**2 * x % mod
    
def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def div(a, b):
    return mul(a, power(b, mod-2))
def div2(a, b):
    return mul(a, modinv(b))

def modinv(a):
    b, u, v = mod, 1, 0
    while b:
        t = a//b
        a, u = a-t*b, u-t*v
        a, b, u, v = b, a, v, u
    u %= mod
    return u

def cmb(n, r):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r]
K, = map(int, input().split())
N = 3
B = [0] * (K+1)
r = 0
for i in range(K, 0, -1):
    ac = K//i
    c = power(ac, N)
    bsum = 0
    for j in range(ac-1):
        j += 2
        bsum += B[i*j]
    B[i] = (c - bsum)%mod
    r = (r+B[i]*i)%mod
print(r)

