ROOT = 3
MOD = 998244353
roots  = [pow(ROOT,(MOD-1)>>i,MOD) for i in range(24)] # 1 の 2^i 乗根
iroots = [pow(x,MOD-2,MOD) for x in roots] # 1 の 2^i 乗根の逆元

def untt(a,n):
    for i in range(n):
        m = 1<<(n-i-1)
        for s in range(1<<i):
            w_N = 1
            s *= m*2
            for p in range(m):
                a[s+p], a[s+p+m] = (a[s+p]+a[s+p+m])%MOD, (a[s+p]-a[s+p+m])*w_N%MOD
                w_N = w_N*roots[n-i]%MOD

def iuntt(a,n):
    for i in range(n):
        m = 1<<i
        for s in range(1<<(n-i-1)):
            w_N = 1
            s *= m*2
            for p in range(m):
                a[s+p], a[s+p+m] = (a[s+p]+a[s+p+m]*w_N)%MOD, (a[s+p]-a[s+p+m]*w_N)%MOD
                w_N = w_N*iroots[i+1]%MOD
            
    inv = pow((MOD+1)//2,n,MOD)
    for i in range(1<<n):
        a[i] = a[i]*inv%MOD

def convolution(a,b):
    deg = len(a) + len(b) - 2
    n = deg.bit_length()
    N = 1<<n
    a += [0]*(N-len(a))
    b += [0]*(N-len(b))
    untt(a,n)
    untt(b,n)
    for i in range(N):
      a[i] = a[i]*b[i]%MOD
    iuntt(a,n)
    return a[:deg+1]

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = convolution(a,b)
print(*c)