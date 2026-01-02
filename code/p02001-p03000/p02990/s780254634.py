def solve():
    N, K = map(int,input().split())
    MOD = 10 ** 9 + 7
    fac, finv, inv = COMinit(N+1,MOD)
    ans = []
    for i in range(1,K+1):
        com1 = COM(K-1,i-1,MOD,fac,finv,inv)
        if N-K-(i-1) < 0:
            ans.append(0)
            continue
        com2 = COM(N-K+1,N-K-(i-1),MOD,fac,finv,inv)
        ans.append(com1*com2%MOD)
    
    print(*ans,sep='\n')

# COMの前処理
# テーブルを作る
# O(n)
def COMinit(N, mod):
    fac = [0] * N
    finv = [0] * N
    inv = [0] * N

    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1

    for i in range(2, N):
        fac[i] = fac[i-1] * i % mod
        inv[i] = mod - inv[mod%i] * (mod // i) % mod
        finv[i] = finv[i-1] * inv[i] % mod
    
    return fac, finv, inv

# nCrを計算 前処理としてCOMinitの実行が必要
# O(1)
def COM(n, r, mod, fac, finv, inv):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n-r] % mod) % mod

if __name__ == '__main__':
    solve()