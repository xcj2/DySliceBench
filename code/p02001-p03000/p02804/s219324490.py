def factorials(n,mod=10**9+7):
    # 0~n!のリスト
    f = [1,1]
    for i in range(2,n+1):
        f.append(f[-1]*i%mod)

    # 0~n!の逆元のリスト
    g = [1]
    for i in range(n):
        g.append(pow(f[i+1],mod-2,mod))

    return f,g


def combination_mod(f,g,n,r,mod=10**9+7):
    # nCr mod modを求める
    nCr = f[n] * g[n-r] * g[r]
    nCr %= mod
    return nCr


def permutation_mod(f,g,n,r,mod=10**9+7):
    # nPr mod modを求める
    nPr = f[n] * g[n-r]
    nPr %= mod
    return nPr


n,k = map(int, input().split())
a = list(map(int, input().split()))
m = 10**9+7

a.sort()

f,g = factorials(n)
ans = 0

for i in range(k-1,n):
    ans += combination_mod(f,g,i,k-1)*a[i]
for i in range(n-k+1):
    ans -= combination_mod(f,g,n-i-1,k-1)*a[i]
while ans < 0:
    ans += m
print(ans%m)


