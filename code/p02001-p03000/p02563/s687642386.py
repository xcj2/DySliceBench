ROOT = 3
MOD = 998244353
pn = [pow(ROOT,(MOD-1)>>i,MOD) for i in range(30)]

def ntt_rec(a,n):
    if n==0:
        return a[:]
    if n==1:
        return [a[0]+a[1],a[0]-a[1]]

    b = ntt_rec(a[::2],n-1)
    c = ntt_rec(a[1::2],n-1)
    
    N = 1<<(n-1)
    res = [0]*(N*2)
    w_N = 1
    for k in range(N):
        res[k]   = (b[k] + w_N*c[k])%MOD
        res[k+N] = (b[k] - w_N*c[k])%MOD
        w_N = w_N*pn[n]%MOD
    return res

def intt_rec(a,n):
    res = ntt_rec(a[0:1]+a[1:][::-1],n)
    inv = pow(1<<n,MOD-2,MOD)
    for i in range(1<<n):
        res[i] = res[i]*inv%MOD
    return res


def convolution(a,b):
    deg = len(a) + len(b) - 1
    n = 0
    N = 1
    while deg*2 >= N:
        n += 1
        N <<= 1
    
    a += [0]*(N-len(a))
    b += [0]*(N-len(b))
    
    #print(ntt_rec(a,n))
    return intt_rec([ai*bi%MOD for ai,bi in zip(ntt_rec(a,n),ntt_rec(b,n))],n)

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
#*a, = [1]*10**5
#*b, = [1]*10**5
L = len(a)+len(b)
c = convolution(a,b)
print(*c[:L-1])
