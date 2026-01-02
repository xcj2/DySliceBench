from sys import stdin
input = stdin.readline

MOD = 10**9 + 7





def solve():
    N,M = map(int,input().split())
    # print(cntA*dp(M,N)%MOD)
    fac = [1,1] + [0] * M
    inv = [1,1] + [0] * M
    for i in range(2,M+1):
        fac[i] = (fac[i-1]*i)%MOD
    inv[M] = pow(fac[M],MOD-2,MOD)
    for i in range(M-1,1,-1):
        inv[i] = inv[i+1]*(i+1)%MOD
    def p(a,b):
        return (fac[b]*inv[b-a])%MOD
    def c(a,b):
        return (fac[b]*inv[a]*inv[b-a]) % MOD
    res = p(N,M)
    for i in range(1,N+1):
        res += (-1)**(i&1)*c(i,N)*p(N-i,M-i)
        res %= MOD
    print(res* p(N,M)%MOD)




if __name__ == '__main__':
    solve()
