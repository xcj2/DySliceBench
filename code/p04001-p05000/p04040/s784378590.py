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

H,W,A,B = map(int,input().split())
H -= 1
W -= 1
A -= 1
B -= 1

init(10**6)

def cal(i,j):
    return comb(i+j,i)

ans = 0
for i in range(H-A):
    ans += comb(B+i,i) * comb(W-B-1+H-i,H-i)

ans %= mod
print(ans)