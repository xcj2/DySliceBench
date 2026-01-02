import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template


# BEGIN CUT HERE
MOD = 10**9 + 7
# MOD = 998244353  # AGC025_B


class Modint():
    '''
    自動でMODで割った余りを計算してくれる整数。MODは素数である必要があり，デフォルトは10**9+7。
    Parameters
    ----------
        n (int) : Modintの初期値
        MOD=10^9+7 (int) : 余りを計算するMOD。素数である必要がある。
    Methods
    ----------
        inverse(n: int) -> Modint
            n の逆元を返す。
    '''

    def __init__(self, n: int, mod=MOD):
        if n >= 0:
            self.n = n % mod
        else:
            self.n = (mod - (-n) % mod) % mod
        self.mod = mod

    def __eq__(self, other):
        return self.n == int(other)

    def __ne__(self, other):
        return not self == other

    def __neg__(self):
        return self.__class__(-self.n)

    def __str__(self):
        return str(self.n)

    def __int__(self):
        return self.n

    def __iadd__(self, other):
        self.n += int(other)
        self.n %= self.mod
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        self.n -= int(other)
        self.n %= self.mod
        return self

    def __rsub__(self, other):
        return self.__sub__(other)

    def __imul__(self, other):
        self.n = self.n * int(other) % self.mod
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def inverse(self):
        '''
        フェルマーの小定理を考えると，MOD-2乗することでMODでの逆元を求めることができる。これは組み込み関数のpowを使うと十分に早い（O(log MOD)）。
        '''
        return self.__class__(pow(self.n, self.mod - 2, self.mod))

    def __ifloordiv__(self, other):
        self *= pow(int(other), self.mod - 2, self.mod)
        return self

    def __rfloordiv__(self, other):
        return self.__class__(other).__floordiv__(self)

    def __add__(self, other):
        return self.__class__(self.n + int(other))

    def __sub__(self, other):
        return self.__class__(self.n - int(other))

    def __mul__(self, other):
        return self.__class__(self.n * int(other))

    def __floordiv__(self, other):
        return self.__class__(self.n * Modint(int(other)).inverse())

    # def comb(self, n: int, k: int):
    #     '''
    #     コンビネーション絡みの定義。comb(n,k):特に前処理をせずnCkを求める
    #     毎回O(N)かかるので死ぬ覚悟でO(N^2)を投げるくらいしか無理

    #     ちなみにですが，これでABC132_D()を出すとPyPy3で1932msくらいですれすれセーフ
    #     '''
    #     if n < k or k < 0:
    #         return Modint(0)
    #     res = Modint(1)
    #     for i in range(int(k)):
    #         res *= Modint(n - i)
    #         res //= Modint(i + 1)
    #     return res

    # def H(self, n: int, k: int):
    #     if n < 0 or k < 0:
    #         return Modint(0)
    #     elif n == 0 and k == 0:
    #         return Modint(1)
    #     else:
    #         return self.comb(n + k - 1, n)


COMBINATION_MAX = 2 * 10**5


class Combination():
    def __init__(self, sz=COMBINATION_MAX):
        '''
        Nまでの階乗とその逆元（割り算用）を計算しておく。前処理にO(N)，P, C, Hそれぞれの計算はO(1)。N = 200000なら割と余裕で通る。
        '''
        self._fact = [Modint(0)] * (sz + 1)
        self._rfact = [Modint(0)] * (sz + 1)
        self._fact[0] = Modint(1)
        self._rfact[sz] = Modint(1)
        for i in range(1, sz + 1):
            self._fact[i] = self._fact[i - 1] * Modint(i)
        self._rfact[sz] = self._fact[sz].inverse()
        for i in range(sz - 1, -1, -1):
            self._rfact[i] = self._rfact[i + 1] * Modint(i + 1)

    def fact(self, k: int) -> int:
        return self._fact[k]

    def rfact(self, k: int) -> int:
        return self._rfact[k]

    def P(self, n: int, k: int) -> Modint:
        '''
        nPkの値を返す。nはあらかじめ前処理されたN以下でないとダメ
        Parameters
        ----------
            n (int) : nPkのn (0<=n<=N)
            k (int) : nPkのk （0<=k<=n）
        Returns
        ----------
            Modint : nPkをModint型で返す。Modintに依存。
        '''
        if k < 0 or n < k:
            return 0
        return self._fact[n] * self._rfact[n - k]

    def C(self, n: int, k: int) -> Modint:
        '''
        nCkの値を返す。nはあらかじめ前処理されたN以下でないとダメ
        Parameters
        ----------
            n (int) : nCkのn(0<=n<=N)
            k (int) : nCkのk（0<=k<=n）
        Returns
        ----------
            Modint : nCkをModint型で返す。Modintに依存。
        '''
        if k < 0 or n < k:
            return 0
        if n - k < k:
            k = n - k
        return self._fact[n] * self._rfact[k] * self._rfact[n - k]

    def H(self, n: int, k: int) -> Modint:
        '''
        nHkの値を返す。nはあらかじめ前処理されたN以下でないとダメ

        ちなみにnHkはn個の区別できないものをk個の箱に分けるパターンの数で，結局n+k-1Cnになる。
        Parameters
        ----------
            n (int) : nHkのn(0<=n<=N)
            k (int) : nHkのk（0<=k<=n）
        Returns
        ----------
            Modint : nHkをModint型で返す。Modintに依存。
        '''
        if n < 0 or k < 0:
            return 0
        elif k == 0:
            return 1
        return self.C(n + k - 1, k)

# END CUT HERE


def ABC021_D():
    n = ii()
    k = ii()
    res = Combination()
    print(res.H(n, k))
# verified on 2019/07/01
# https://atcoder.jp/contests/abc021/tasks/abc021_d
# PyPy3: 243ms https://atcoder.jp/contests/abc021/submissions/6207045


def ABC132_D():
    N, K = mi()
    res = Combination(N)
    for i in range(1, K + 1):
        print(res.C(K - 1, i - 1) * res.C(N - K + 1, i))
# verified on 2019/07/01
# https://atcoder.jp/contests/abc132/tasks/abc132_d
# Python3: 32ms https://atcoder.jp/contests/abc132/submissions/6200580
# PyPy3だとオーバヘッドが大きいのか240msくらいかかるけど，基本はPyPyで良いと思う。


def AGC025_B():
    N, A, B, K = mi()
    res = Combination(N)
    ans = Modint(0)
    for a in range(min(K // A + 1, N + 1)):
        b = (K - a * A) // B
        if A * a + B * b == K and a >= 0 and b >= 0:
            ans += res.C(N, a) * res.C(N, b)
    print(ans)
# verified on 2019/07/01
# https://atcoder.jp/contests/agc025/tasks/agc025_b
# PyPy3: https://atcoder.jp/contests/agc025/submissions/6200598
# Python3だとTLE


def ABC130_E():
    N, M = mi()
    S = lmi()
    T = lmi()
    a = [[Modint(0) for __ in range(M + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(M + 1):
            if i == 0 or j == 0:
                a[i][j] = Modint(1)
            else:
                a[i][j] = a[i - 1][j] + a[i][j - 1] - \
                    (a[i - 1][j - 1] if S[i - 1] != T[j - 1] else 0)
    print(a[N][M])
# verified on 2019/07/01
# https://atcoder.jp/contests/abc130/tasks/abc130_e
# PyPy3: 1839ms https://atcoder.jp/contests/abc130/submissions/6204339
# やっぱりクソ遅い


if __name__ == '__main__':
    # ABC021_D()
    # ABC132_D()
    # AGC025_B()
    ABC130_E()
