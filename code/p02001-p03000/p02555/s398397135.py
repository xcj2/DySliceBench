
#逆元

def inverse(a,mod): #aのmodを法にした逆元を返す
    return pow(a,mod-2,mod)



#modのn!と、n!の逆元を格納したリストを返す(拾いもの)
#factorialsには[1, 1!%mod , 2!%mod , 6!%mod… , n!%mod] が入っている
#invsには↑の逆元が入っている

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


def modnCr(n,r,mod,fac,inv): #上で求めたfacとinvsを引数に入れるべし(上の関数で与えたnが計算できる最大のnになる)

    return fac[n] * inv[n-r] * inv[r] % mod

S = int(input())

mod = 10**9+7

ans = 0
fac,inv = modfac(S+10,mod)

for N in range(1,S):

    if S - 3*N < 0:
        break

    rem = S - 3*N
    ans += modnCr( rem + N - 1 , N-1 , mod,fac,inv )

print (ans % mod)
