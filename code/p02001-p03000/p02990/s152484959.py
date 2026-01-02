mod = 10**9 + 7

def init(n):
    # 階乗とその逆元をグローバルに定義
    global factorial, inverse
    # 0-indexedでそれぞれ１で初期化
    factorial = [1]*(n+1)
    inverse = [1]*(n+1)

    fact = 1 
    for p in range(1,n+1):
        fact *= p
        fact %= mod
        factorial[p] = fact
    
    inv = pow(fact, mod-2, mod)
    inverse[n] = inv
    for p in range(2,n+1)[::-1]:
        inv *= p
        inv %= mod
        inverse[p-1] = inv

def comb(n,r):
    if n < r:
        return 0
    return factorial[n] * inverse[n-r] * inverse[r] % mod

N,K = map(int,input().split())

def cal(i):
    return comb(K-1,i-1) * comb(N-K+1,i) % mod

init(10**4)

for i in range(1,K+1):
    ans = cal(i)
    print(ans)