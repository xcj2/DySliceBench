import sys
P = int(input())
As = list(map(int, input().split()))
rs = [0]*P
mod = P
sys.setrecursionlimit(pow(10, 8))

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y//2)**2 % mod
    else            : return power(x, (y-1)//2)**2 * x % mod
    
def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def div(a, b):
    return mul(a, power(b, mod-2))

def cmb(n, r):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

NNN = 3000
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
for i in range( 2, NNN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
C = []
for i in range(P):
    C.append(cmb(P-1, i))


for i in range(P):
    if As[i]:
        rs[0] += 1
        tmp = 1
        for k in range(P):
            k = P-1-k
            rs[k] += (-1 + 2*(k%2)) * tmp * C[k]
            rs[k] %= mod
            tmp = tmp * i % mod
print(*rs)

