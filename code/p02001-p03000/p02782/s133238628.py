MAX = 2*10**6+100
fact = [0]*MAX
inv = [0]*MAX
finv = [0]*MAX
 
def C_init():
    fact[0] = 1
    fact[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    
    for i in range(2, MAX):
        fact[i] = fact[i-1]*i%MOD
        inv[i] = MOD-inv[MOD%i]*(MOD//i)%MOD
        finv[i] = finv[i-1]*inv[i]%MOD
 
def C(n, r):
    if n<r:
        return 0
    if n<0 or r<0:
        return 0
    return fact[n]*(finv[r]*finv[n-r]%MOD)%MOD

def g(r, c):
    return ((r+2)*C(c+r+2, r+2)-c-1)*inv[c+1]

r1, c1, r2, c2 = map(int, input().split())
MOD = 10**9+7
C_init()
ans = g(r2, c2)-g(r2, c1-1)-g(r1-1, c2)+g(r1-1, c1-1)
ans %= MOD

print(ans)