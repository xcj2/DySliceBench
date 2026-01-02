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
mn = 0
ma = 0
a = list(map(int,input().split()))
a.sort()
mod = 10**9 + 7
c = 1
for i in range(n-k+1):
    mn += a[n-k-i]*c
    ma += a[k-1+i]*c
    c = c*(k+i)%mod
    c = c*mod_inv(i+1,mod)%mod
print((ma-mn)%mod)