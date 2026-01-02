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
def modinv(a):
    b, u, v = mod, 1, 0
    while b:
        t = a//b
        a, u = a-t*b, u-t*v
        a, b, u, v = b, a, v, u
    u %= mod
    return u
def div(a, b):
    return a * modinv(b) % mod

def G(n, i):
    if n == 1:
        return 1
    tn = n//2
    return (G(tn, i) * (1 + power(10, tn*i)) %mod + (n%2)*power(10, (n-1)*i)) % mod

def G2(n, i):
    if n ==0 :
        return 0
    if n == 1:
        return power(10, i) % mod
    tn = n//2
    X = G2(tn, i)
    I = power(10, tn*i)
    Y = (X*(I+1)%mod + mul(mul(tn, I), (G(tn+1, i)-1))%mod) %mod
    Y = Y + mul(n%2, mul(n, power(10, n*i)))
    return Y%mod


def f(a, b, n, i):
    if n == 0:
        return 0
    r = power(10, i)
    P = power(r,n)
    #aa = mul(a, div(P-1, r-1))
    aa = mul(a, G(n, i))
    bb2 = mul(b, div(r-n*P + (n-1)*P*r, mul(1-r, 1-r)))
    bb = mul(b, G2(n-1, i))
    #print(n-1, i, div(r-n*P + (n-1)*P*r, mul(1-r, 1-r)), G2(n-1, i))
    #print(bb, bb2)
    return (aa - bb) % mod

sl = A + (L-1) * B
t = 10
k = 0
ts = 0
ks = []
mk = 18
for i in range(mk):
    k = max(min((t-1),sl)-(A-B), 0) // B - ts
    #print(t, min(t, sl) - (A-B), -(-((min(t, sl) - (A-B))//B)))
    #k = -(-(min(t, sl) - (A-B)) // B) - 1 - ts
    ts += k
    ks.append(k)
    t *= 10
ti = 0
ti2 = 0
b = B
R = 0
for i in range(mk):
    i = mk - i
    n = ks[i-1]
    a = sl - ti2*b
    if n:
        R = (R + (f(a, b, n, i))*power(10, ti)) % mod
#        print(a, f(a,b,r,n))
#    print(a, b, r, n, R, ti)

    ti += i*n
    ti2 += n
print(R)
#$print(ks)
