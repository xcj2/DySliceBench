import sys
from collections import deque
def input(): return sys.stdin.readline().strip()
mod = 10**9+7

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


comb = Combination(5 * 10**5)


def main():
    """
    「異なる」はネガティブだから逆を考えるべきなのか。。。
    そうすると包除原理が浮かんできそう
    A=[1,2,...,N]は仮定してよい。後で{}_M P_Nをかければよい。
    """
    N, M = map(int, input().split())
    ans = 0
    for i in range(N + 1):
        """
        B[j] = jなるものがi箇所ある場合。
        まずB[j] = jなるi箇所を選ぶためにcomb(N, i)必要。
        そのあとそれ以外の場所(N - i)箇所に埋める数を(M - i)個から選ぶための{}_{M-i} P_{N - i}が必要。
        """
        val = comb(N, i) * comb(M - i, N - i) * comb.fac[N - i] * (-1) ** i
        ans += val % mod
        #print("i={}, val={}".format(i, val))
    ans *= comb(M, N) * comb.fac[N]
    print(ans % mod)
    

if __name__ == "__main__":
    main()
