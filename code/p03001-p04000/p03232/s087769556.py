
import sys
from itertools import accumulate
mod = pow(10, 9) + 7
N, = [int(i) for i in input().split(' ')]
As = [int(i) for i in input().split(' ')]
sys.setrecursionlimit(pow(10, 8))

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y//2)**2 % mod
    else            : return power(x, (y-1)//2)**2 * x % mod

NNN = 10**5
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range( 2, NNN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

def fractional(N):
    if N == 0:
        return 1
    else:
        return mul(N, fractional(N-1))

T = g1[N]
fracs = list(accumulate([0] + [mul(T, inverse[(i+1)]) for i in range(N)]))


result = 0
for i in range(N):
    i = i+1
    x = mul(As[i-1], fracs[N-i+1] + (fracs[i] - fracs[1]))
    result = (result + x) % mod 
print(result)
