import sys

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


n,k = map(int,input().split())
mod = 10**9+7

fac,inv = modfac(2*n,mod)
"""
nm1lis = [1]
for i in range(n):
    nm1lis.append(nm1lis[-1] * (n-1) % mod)

print (nm1lis)
"""

if k >= n:
    print (modnCr(2*n-1,n,mod,fac,inv))
    sys.exit()

"""
求めるのは人数の組み合わせ
どうする？
不可能なものの数を数えて引くか？
k+2以上の人数の部屋があったら不可能
k+2人以上が1つあるときの組み合わせ- (2つあるときの組み合わせ) + …

でいけそうかな？
それ以外は可能なのか？

0の数がk恋かの組み合わせ
0の数がk個より大きいなら不可能

0がk+1個…Nこ
"""

ans = modnCr(2*n-1,n,mod,fac,inv)
loop = 1

for i in range(k+1,n):

    bn = n - i - 1
    now = modnCr(n,i,mod,fac,inv) * modnCr(i+bn,bn,mod,fac,inv)

    ans -= now
    
    ans %= mod

    loop += 1

print (ans)

"""

while (k+2)*loop <= n:

    now = modnCr(n,loop,mod,fac,inv) * modnCr(n-1 + (n-(k+2)*loop),n-1,mod,fac,inv)
    if loop % 2 == 1:
        ans -= now
    else:
        ans += now

    ans %= mod

    loop += 1

"""
    