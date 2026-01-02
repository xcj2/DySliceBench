import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N, M = map(int,input().split())

mod = 10 ** 9 + 7
MAX = max(M,N)+10
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
def permu(n,r):
    return fac[n] * finv[n-r]

cominit()

ans = permu(M, N)%mod
minus = 0
for i in range(1, N+1):
    minus += (-1)**((i-1)&1)*cmb(N,i)*permu(M-i, N-i)
    minus %= mod
ans += mod - minus
ans %= mod
ans *= permu(M,N)
ans %= mod
print(ans)