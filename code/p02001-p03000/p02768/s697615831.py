n,a,b = map(int, input().split())
mod = 10**9 + 7
def power_(n, p, mod):
    if p == 1:
        return n
    if p % 2 == 0:
        return (power_(n, p//2, mod) ** 2) % mod
    else:
        return n * (power_(n, p//2, mod) ** 2) % mod
#互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
#a/b = a*(b`)となるb`を求める
def mod_inv(a,mod):
    x = extgcd(a,mod)[0]
    return (mod+x%mod)%mod
def mod_cmb(p,q,mod):
    #pCqを計算
    res = 1
    for i in range(q):
        res *= (p - i) * mod_inv(q - i, mod)
        res %= mod
    return res % mod
p = power_(2,n, mod)
sub = mod_cmb(n,a,mod) + mod_cmb(n,b,mod)
print((p - sub - 1) % mod)