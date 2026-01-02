mod = 998244353
omega = pow(3,119,mod)
rev_omega = pow(omega,mod-2,mod)

N = 2*10**5
g1 = [1]*(N+1) # 元テーブル
g2 = [1]*(N+1) #逆元テーブル
inv = [1]*(N+1) #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1[i]=( ( g1[i-1] * i ) % mod )
    inv[i]=( ( -inv[mod % i] * (mod//i) ) % mod )
    g2[i]=( (g2[i-1] * inv[i]) % mod )
inv[0]=0

def _ntt(f,L,reverse=False):
    F=[f[i] for i in range(L)]
    n = L.bit_length() - 1
    base = omega
    if reverse:
        base = rev_omega

    if not n:
        return F

    size = 2**n
    wj = pow(base,2**22,mod)
    res = [0]*2**n

    for i in range(n,0,-1):
        use_omega = pow(base,2**(22+i-n),mod)
        res = [0]*2**n
        size //= 2
        w = 1
        for j in range(0,L//2,size):
            for a in range(size):
                res[a+j] = (F[a+2*j] + w * F[a+size+2*j]) % mod
                t = (w * wj) % mod
                res[L//2+a+j] = (F[a+2*j] + t * F[a+size+2*j]) % mod
            w = (w * use_omega) % mod
        F = res

    return res

def ntt(f,L=0):
    l = len(f)
    if not L:
        L = 1<<((l-1).bit_length())
    while len(f)<L:
        f.append(0)
    f=f[:L]
    F = _ntt(f,L)
    return F

def intt(f,L=0):
    l = len(f)
    if not L:
        L = 1<<((l-1).bit_length())
    while len(f)<L:
        f.append(0)
    f=f[:L]
    F = _ntt(f,L,reverse=True)
    inv = pow(L,mod-2,mod)
    for i in range(L):
        F[i] *= inv
        F[i] %= mod
    return F

def convolve(f,g,limit):
    l = len(f)+len(g)-1
    L = 1<<((l-1).bit_length())

    F = ntt(f,L)
    G = ntt(g,L)

    H = [(F[i] * G[i]) % mod for i in range(L)]

    h = intt(H,L)

    return h[:limit]

N,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

print(*convolve(a,b,N+M-1))