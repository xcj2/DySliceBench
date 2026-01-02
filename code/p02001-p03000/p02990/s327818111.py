N,K = map(int,input().split())


mod = 10 ** 9 + 7
MAX = N+K
fac = [0] * MAX
finv = [0] * MAX
inv = [0] * MAX

def cominit():
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    for i in range(2,MAX):
        fac[i] = fac[i-1] * i % mod
        inv[i] = mod - inv[mod%i] * (mod//i) % mod
        finv[i] = finv[i-1] * inv[i] % mod



def cmb(n,r):
    if n < 0 or r < 0 or r > n:return 0
    if r > n/2: r = n-r        
    return fac[n] * (finv[r] * finv[n-r] % mod) % mod
    
cominit()
'''
def cmb(n,k):
    if k>n:
        return 0
    elif k > (n+1)/2:
        return cmb(n,n-k)
    tmp = 1
    for i in range(n-k+1,n+1):
        tmp *= i
    for i in range(1,k+1):
        tmp //= i
    tmp %= mod
    return tmp    
'''        
    
for i in range(1,K+1):
    cr = cmb(N-K+1,i)
    cb = cmb(K-1,i-1)
    ans = cr*cb
    ans %= mod
    print(ans)
    