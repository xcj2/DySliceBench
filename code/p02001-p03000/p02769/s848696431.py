def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2] != 1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    return [w[0],w[1]]
def mod_inv(a,mod):
    x = extgcd(a,mod)[0]
    return (mod + x % mod)% mod
def comb(n,k,mod):
    c = 1
    for i in range(k):
        c = c*(n-i)%mod
        c = c*mod_inv(i+1,mod)%mod
    return c
n,k = map(int,input().split())
mod = 10**9+7
if k >= n-1:
    print(comb(n+n-1,n,mod))
else:
    ans = 0
    c = 1
    c2 = 1
    for i in range(k):
        c = c*(n-1-i)%mod
        c2 = c2*(n-i)%mod
        c = c*mod_inv(i+1,mod)%mod
        c2 = c2*(mod_inv(i+1,mod))%mod
        ans += c*c2
        ans %= mod
    if k > 1:
        ans += 1
    print(ans)