from collections import defaultdict

class Combination:
    """
    O(n)の前計算を1回行うことで，O(1)でnCr mod mを求められる
    n_max = 10**6のとき前処理は約950ms (PyPyなら約340ms, 10**7で約1800ms)
    使用例：
    comb = Combination(1000000)
    print(comb(5, 3))  # 10
    """
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        self.fac, self.facinv = self.make_factorial_list(n_max)

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    def make_factorial_list(self, n):
        # 階乗のリストと階乗のmod逆元のリストを返す O(n)
        # self.make_modinv_list()が先に実行されている必要がある
        fac = [1]
        facinv = [1]
        for i in range(1, n+1):
            fac.append(fac[i-1] * i % self.mod)
            facinv.append(facinv[i-1] * self.modinv[i] % self.mod)
        return fac, facinv

    def make_modinv_list(self, n):
        # 0からnまでのmod逆元のリストを返す O(n)
        modinv = [0] * (n+1)
        modinv[1] = 1
        for i in range(2, n+1):
            modinv[i] = self.mod - self.mod//i * modinv[self.mod%i] % self.mod
        return modinv

def main():
    #def cmb(n, r, mod):
    #    if ( r<0 or r>n ):
    #        return 0
    #    r = min(r, n-r)
    #    return g1[n] * g2[r] * g2[n-r] % mod
#
    #mod = 10**9+7 #出力の制限
    #N = 10**4
    #g1 = [1, 1] # 元テーブル
    #g2 = [1, 1] #逆元テーブル
    #inverse = [0, 1] #逆元テーブル計算用テーブル
#
    #for i in range( 2, N + 1 ):
    #    g1.append( ( g1[-1] * i ) % mod )
    #    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    #    g2.append( (g2[-1] * inverse[-1]) % mod )
    
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    mod = 10 ** 9 + 7
    comb = Combination(1000000)
    # 最小になる数を求める
    for i, a in enumerate(A):
        if (N - 1 - i) >= K-1:
            #tmp = cmb(N-1-i,K-1,mod)
            tmp = comb(N-1-i, K-1)
            ans -= (a * tmp)
            ans %= mod
        else:
            break
    
    A.sort(reverse=True)
    for i, a in enumerate(A):
        if (N - 1 - i) >= K-1:
            #tmp = cmb(N-1-i,K-1,mod)
            tmp = comb(N-1-i, K-1)
            ans += (a * tmp)
            ans %= mod
        else:
            break

    print(ans)

    
    

if __name__ == "__main__":
    main()