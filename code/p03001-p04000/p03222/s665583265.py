import sys
from functools import lru_cache
def input(): return sys.stdin.readline().strip()
mod = 1000000007

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

@lru_cache(maxsize=None)
def calc(n):
    """
    n個のものから隣り合わないように物をいくつか選択する場合の数(何も選ばないケースも許す)
    これは実はフィボナッチ数列になる
    """
    if n == -1: return 1
    if n == 0: return 1
    if n == 1: return 2
    return (calc(n - 1) + calc(n - 2)) % mod

@lru_cache(maxsize=None)
def func(h, w, k):
    if h == 0 and k == 1: return 1
    if h == 0: return 0
    if k == 1:
        val1 = func(h - 1, w, 1) * calc(w - 2) % mod
        val2 = func(h - 1, w, 2) * calc(w - 3) % mod
        return (val1 + val2) % mod
    if k == w:
        val1 = func(h - 1, w, w) * calc(w - 2) % mod
        val2 = func(h - 1, w, w - 1) * calc(w - 3) % mod
        return (val1 + val2) % mod
    val1 = func(h - 1, w, k - 1) * calc(k - 3) * calc(w - (k + 1)) % mod
    val2 = func(h - 1, w, k) * calc(k - 2) * calc(w - (k + 1)) % mod
    val3 = func(h - 1, w, k + 1) * calc(k - 2) * calc(w - (k + 2)) % mod
    return (val1 + val2 + val3) % mod

def main():
    H, W, K = map(int, input().split())
    if W == 1:
        print(1)
        return
    if W == 2:
        comb = Combination(H)
        if K == 1:
            ans = 0
            for i in range(H // 2 + 1): ans += comb(H, i * 2)
            print(ans)
        else:
            ans = 0
            for i in range(1, (H + 1) // 2 + 1): ans += comb(H, i * 2 - 1)
            print(ans)
        return
    print(func(H, W, K))
    

    




if __name__ == "__main__":
    main()
