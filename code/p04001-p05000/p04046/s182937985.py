
#modの掛け算
 
def modmal(a,b,mod): #a*bをmodを法にして求める
 
    return a * b % mod
 
 
#modの割り算
 
def moddiv(a,b,mod): #a/bをmodを法にして求める
 
    return (a * pow(b,mod-2)) % mod
 
 
#逆元
 
def inverse(a,mod): #aのmodを法にした逆元を返す
    return pow(a,mod-2)
 
 
 
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
 
 
def modnCr(n,r,mod,fac,inv): #上で求めたfacとinvsを引数に入れるべし
 
    return fac[n] * inv[n-r] * inv[r] % mod


H,W,A,B = map(int,input().split())

mod = 10 ** 9 + 7
ans = 0

fac,inv = modfac(H+W,mod)

for i in range(H-A):

    now = modnCr(i + B-1, i,mod,fac,inv)
    now *= modnCr(H+W-i-B-2,W-B-1,mod,fac,inv)

    ans += now
    ans %= mod

print (ans)
