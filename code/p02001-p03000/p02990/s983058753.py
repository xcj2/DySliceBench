def framod(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a

def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod

def comb(n, k, mod):
    if n == k:
        return 1
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod

mod = 10**9+7
N, K = map(int,input().split())
for i in range(1,K+1):
    if (N-K+1) < i:
        print(0)
        continue
    # 白部分を分割する
    pt_base = comb(N-K+1,i,mod)
    #分割部分に1個以上ものを入れる
    # 任意に入れれるものの個数
    ct = K - i
    # あとはランダム
    pt = comb(K-1 ,i-1  , mod)
    res = ((pt_base % mod) * (pt % mod)) % mod 
    print(res)