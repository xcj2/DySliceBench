"""

手の付け方がわからない
ある条件を決める中での余事象？
A != Bでおいていく
毎回横で被る場合を引く

←にk個置かれてて
* MC2　したとする
上側に置いたのがかぶってる確率は (k / M)
下側もそう
両側は (k/M)**2

dp[k+1] = dp[k] * MC2 * (1 - 2*(k/M) + (k/M)**2)

Aを置いた
Bを置く　→　ほう助原理

"""

def inverse(a,mod): #aのmodを法にした逆元を返す
    return pow(a,mod-2,mod)

def modfac(n, MOD):
 
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return factorials, invs


def modnCr(n,r): #上で求めたfacとinvsを引数に入れるべし(上の関数で与えたnが計算できる最大のnになる)

    return fac[n] * inv[n-r] * inv[r] % mod


N,M = map(int,input().split())
mod = 10**9+7

fac,inv = modfac(5*10**5+10,mod)

las = fac[N] * modnCr(M,N)

now = 0
for i in range(N+1):

    np = modnCr(N,i) * fac[N-i] * modnCr(M-i,N-i)
    if i % 2 == 0:
        now += np
    else:
        now -= np
    #print (np)
    now %= mod

#print (las,now)
print (las * now % mod)
