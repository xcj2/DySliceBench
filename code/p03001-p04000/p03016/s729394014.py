import sys
L, A, B, M = map(int, input().split())
mod = M
sys.setrecursionlimit(pow(10, 8))

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y//2)**2 % mod
    else            : return power(x, (y-1)//2)**2 * x % mod
def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def G(n, i):
    # G = 1 + R + (R**2) + (R**3) ... (R**(n-1))
    # R = 10**i
    if n == 1:
        return 1
    tn = n//2
    return (G(tn, i) * (1 + power(10, tn*i)) %mod + (n%2)*power(10, (n-1)*i)) % mod

def G2(n, i):
    # G2 = R + 2(R**2) + 3(R**3) ... n(R**n)
    # R = 10**i
    if n ==0 :
        return 0
    if n == 1:
        return power(10, i) % mod
    tn = n//2
    X = G2(tn, i)
    I = power(10, tn*i)
    Y = (X*(I+1)%mod + mul(mul(tn, I), (G(tn+1, i)-1))%mod) + mul(n%2, mul(n, power(10, n*i)))
    return Y%mod


def f(a, b, n, i):
    if n == 0:
        return 0
    aa = mul(a, G(n, i))
    bb = mul(b, G2(n-1, i))
    return (aa - bb) % mod

SL = A + (L-1) * B
ts = 0
ks = [0]
for i in range(len(str(SL))+1):
    # ks[i] = Count(10**i <= Si <10**(i+1))
    ks.append(max(min((10**(i+1)-1),SL)-(A-B), 0) // B - ts)
    ts += ks[-1]
ti = 0
a = SL
R = 0
# i = 2, n = 3, a = 17, B=2
# 17 * 1500 * 130000
# r += Sum_{0<=j<=n-1}((a-Bj)*pow(10**i, j)) * pow(10, ti)
# j = 0 -> (a+Bj)*pow(10**i, j) = a
for i in range(len(str(SL))+1,0,-1):
    n = ks[i]
    R = (R + f(a, B, n, i)*power(10, ti)) % mod
    ti += i*n
    a -= n*B
print(R)
