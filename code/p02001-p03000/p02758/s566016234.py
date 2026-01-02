import sys
sys.setrecursionlimit(10**6)
from operator import itemgetter
import bisect
def main():
    input = sys.stdin.readline
    N = int(input())
    XD = [tuple(map(int, input().split())) for _ in range(N)]
    MOD = 998244353

    XD.sort(key=itemgetter(0))
    X = [xd[0] for xd in XD]
    segtree = SegmentTree(N+1)
    for i in range(N-1,-1,-1):
        x, d = XD[i]
        j = bisect.bisect_left(X, x+d, i)
        end = max(j-1, segtree.query(i, j))
        segtree.update(i, end)

    dp = [Mint(0, MOD) for _ in range(N+1)]
    dp[N] = Mint(1, MOD)
    for i in range(N-1,-1,-1):
        dp[i] += dp[i+1]
        dp[i] += dp[segtree.get(i) + 1]
    print(dp[0])

class Mint:
    def __init__(self, value=0, mod=10**9+7):
        self.value = ((value % mod) + mod) % mod
        self.mod = mod

    @staticmethod
    def get_value(x): return x.value if isinstance(x, Mint) else x

    def inverse(self):
        a, b = self.value, self.mod
        u, v = 1, 0
        while b:
            t = a // b
            b, a = a - t * b, b
            v, u = u - t * v, v
        return (u + self.mod) % self.mod

    def __repr__(self): return str(self.value)
    def __eq__(self, other): return self.value == other.val
    def __neg__(self): return Mint(-self.value, self.mod)
    def __hash__(self): return hash(self.value)
    def __bool__(self): return self.value != 0

    def __iadd__(self, other):
        self.value = (self.value + Mint.get_value(other)) % self.mod
        return self
    def __add__(self, other):
        new_obj = Mint(self.value, self.mod)
        new_obj += other
        return new_obj
    __radd__ = __add__

    def __isub__(self, other):
        self.value = (self.value - Mint.get_value(other) + self.mod) % self.mod
        return self
    def __sub__(self, other):
        new_obj = Mint(self.value, self.mod)
        new_obj -= other
        return new_obj
    def __rsub__(self, other):
        new_obj = Mint(Mint.get_value(other), self.mod)
        new_obj -= self
        return new_obj

    def __imul__(self, other):
        self.value = self.value * Mint.get_value(other) % self.mod
        return self
    def __mul__(self, other):
        new_obj = Mint(self.value, self.mod)
        new_obj *= other
        return new_obj
    __rmul__ = __mul__

    def __ifloordiv__(self, other):
        other = other if isinstance(other, Mint) else Mint(other, self.mod)
        self *= other.inverse
        return self
    def __floordiv__(self, other):
        new_obj = Mint(self.value, self.mod)
        new_obj //= other
        return new_obj
    def __rfloordiv__(self, other):
        new_obj = Mint(Mint.get_value(other), self.mod)
        new_obj //= self
        return new_obj

class SegmentTree:
    def __init__(self, n=None, f=max, identity_factory=int, initial_values=None):
        assert(n or initial_values)
        size = n if n else len(initial_values)
        d = [identity_factory() for _ in range(2 * size + 1)]
        self.__n, self.__d, self.__f, self.__e = size, d, f, identity_factory
        if initial_values:
            for i, v in enumerate(initial_values): d[size + i] = v
            for i in range(size - 1, 0, -1): d[i] = f(d[i<<1], d[i<<1|1])

    def get(self, index):
        return self.__d[index + self.__n]

    def update(self, index, value):
        i, d, f = index + self.__n, self.__d, self.__f
        if d[i] == value: return
        d[i] = value
        while i:
            i = i >> 1
            d[i] = f(d[i<<1], d[i<<1|1])

    def add(self, index, value):
        self.update(index, self.__f(self.__d[index + self.__n], value))

    def query(self, from_inclusive, to_exclusive):
        ans = self.__e()
        if to_exclusive <= from_inclusive: return ans
        l, r, d, f = from_inclusive + self.__n, to_exclusive + self.__n, self.__d, self.__f
        while l < r:
            if l & 1: ans, l = f(ans, d[l]), l+1
            if r & 1: ans, r = f(d[r-1], ans), r-1
            l, r = l >> 1, r >> 1
        return ans

    def bisect_left(self, func):
        '''func()がFalseになるもっとも左のindexを探す
        '''
        i, n, f, d, v = 1, self.__n, self.__f, self.__d, self.__e()
        while i < n:
            if func(f(v, d[i<<1])): v, i = f(v, d[i<<1]), i<<1|1
            else: i = i<<1
        return i - n

if __name__ == '__main__':
    main()