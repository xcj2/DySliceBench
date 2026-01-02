MOD = 10 ** 9 + 7

def cmb(n, r):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % MOD

def p(n, r):
    return g1[n] * g2[n-r] % MOD

maxN = 5*10**5
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, maxN + 1 ):
    g1.append( ( g1[-1] * i ) % MOD )
    inverse.append( ( -inverse[MOD % i] * (MOD//i) ) % MOD )
    g2.append( (g2[-1] * inverse[-1]) % MOD )

def solve():
    N, M = map(int, input().split())
    ans = 0
    for k in range(N+1):
        x = 0
        tmp = p(M-k, N-k)
        x = cmb(N, k) * p(M, k) * tmp * tmp
        if k%2==1:
            x *= -1
        ans = (ans + x) % MOD
    print(ans)

solve()