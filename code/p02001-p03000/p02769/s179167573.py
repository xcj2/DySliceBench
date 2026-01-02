n, k = map(int, input().split())
mod = 10**9+ 7 
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
fact = [1 for i in range(n*2+1)]
for i in range(1,n*2+1):
    fact[i] = (fact[i-1] * i) % mod
if k + 1 >= n:
    child = fact[n * 2  - 1]
    mother = mod_inv(fact[n], mod) * mod_inv(fact[n-1], mod)
    print((child * mother) % mod)
else:
    #k人までは自由に振り分け、そのあとはnCn-k
    bow = n - k - 1
    """
    child = fact[bow + k]
    mother = (mod_inv(fact[k], mod) * mod_inv(fact[bow], mod)) % mod
    combi = (fact[n] * mod_inv(fact[n - k],mod) * mod_inv(fact[k],mod)) % mod
    aa = power_(n,k,mod)
    aa -= combi
    """
    ans = 0
    #実際に移動する人数を固定
    #ではなく、0人の部屋を固定する
    for i in range(k+1):
        bow = n - i - 1
        child = fact[bow + i]
        mother = (mod_inv(fact[i], mod) * mod_inv(fact[bow], mod)) % mod
        combi = (fact[n] * mod_inv(fact[n - i],mod) * mod_inv(fact[i],mod)) % mod
        ans += (child * mother * combi) % mod
        ans %= mod
    print(ans % mod)