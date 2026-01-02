n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
mod = 10**9+7
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
factorial = [1 for i in range(n+1)]
factorial[0] = 1
for i in range(1,n + 1):
    factorial[i] = factorial[i-1] * i
    factorial[i] %= mod
def mod_combi(a,b):
    if b == 0:
        return 1
    elif a == 0 or a < b:
        return 0
    elif a == b:
        return 1
    else:
        return (factorial[a] * mod_inv(factorial[b], mod) * mod_inv(factorial[a-b],mod)) % mod
ans = 0
#それぞれについて、最小になる場合と最大になる場合をもとめ、ans に加算する。
for i in range(n):
    patt_max = mod_combi(i, k-1)
    patt_min = mod_combi(n-i-1, k-1)
    ans += (patt_max - patt_min) * a[i]
    ans %= mod
print(ans)