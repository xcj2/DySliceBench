mod = 10**9+7
def mul(f,g):
    n = len(f)
    m = len(g)
    h = [0]*(n+m-1)
    for i in range(n):
        for j in range(m):
            h[i+j] += f[i]*g[j]
            h[i+j] %= mod
    return h

def rev(f):
    h = [0]*len(f)
    for i in range(len(f)):
        h[i] += f[i]
        if i%2==1:
            h[i] *= -1
        h[i] %= mod
    return h

def add(f,g):
    if len(f)<len(g):
        f,g = g,f
    g += [0]*(len(f)-len(g))
    h = [0]*len(f)
    for i in range(len(f)):
        h[i] = f[i]+g[i]
        h[i] %= mod
    return h

def coef(n,P,Q):
    if n==0:
        return P[0]%mod
    q = mul(Q,rev(Q))[::2]
    if n%2==0:
        p = mul(P,rev(Q))[::2]
    else:
        p = mul(P,rev(Q))[1::2]
    return coef(n//2,p,q)

P = [0,0,0,0,0,1]
Q = [1]
for i in range(5):
    Q = mul(Q,[1,1])
for i in range(16):
    Q = mul(Q,[1,-1])

T = int(input())
for i in range(T):
    N = int(input())
    print(coef(N,P,Q))