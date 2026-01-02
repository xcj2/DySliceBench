import sys
readline = sys.stdin.buffer.readline
n,k = map(int,readline().split())
mod = 10**9+7
def pow(n,p,mod=10**9+7): #繰り返し二乗法(nのp乗)
    res = 1
    while p > 0:
        if p % 2 == 0:
            n = n ** 2 % mod
            p //= 2
        else:
            res = res * n % mod
            p -= 1
    return res % mod
def factrial_memo(n=10**6+1,mod=10**9+7):
    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)
    return fact
def fermat_cmb(n, r, mod=10**9+7): #needs pow,factrial_memo(only fact). return nCk
    return fact[n] * pow(fact[r],mod-2) * pow(fact[n-r],mod-2) %mod
fact = factrial_memo()

if k > n-1: #全通りの再現が可能ならば
    ans = fermat_cmb(2*n-1,n)
else: #移動回数の制限によって全通りの再現ができないならば
    ans = 1
    for i in range(1,k+1): #全ての動作を再現する(kはたかだか2*10**5である)
        ans += fermat_cmb(n,i)*fermat_cmb(n-1,i)
        #n人の中から動かせる人物をi人取り、n-1箇所(それぞれの人物に付き同じ場所には戻れない)
        #にi人を入れる組み合わせ。それぞれの事象に付き、0人になる部屋と他の部屋の人数は
        #必ず違う組み合わせになるので、これをk回だけ繰り返せば良い
        ans %= mod

print(ans)