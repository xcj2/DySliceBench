# 反転させて扱いやすくしておく S[i]は10^iの個数を表すようになる
S = input()[::-1]

MOD = 10 ** 9 + 7
class modint:
    def __init__(self, x):
        self.x = x.x if isinstance(x, modint) else x % MOD
    def __str__(self): return str(self.x)
    __repr__ = __str__
    def __int__(self): return self.x
    __index__ = __int__
    def __add__(self, other): return modint(self.x + modint(other).x)
    def __sub__(self, other): return modint(self.x - modint(other).x)
    def __mul__(self, other): return modint(self.x * modint(other).x)
    def __pow__(self, other): return modint(pow(self.x, modint(other).x, MOD))
    def __floordiv__(self, other): return modint(self.x * pow(modint(other).x, MOD - 2, MOD))
    def __eq__(self, other): return self.x == modint(other).x
    def __ne__(self, other): return self.x != modint(other).x
    def __inv__(self): return pow(self.x, MOD - 2, MOD)

# 10^i%13を求める
def mod13_of_10pow(i):
    return [1, 10, 9, 12, 3, 4][i % 6]


# ans[k] : 13で割った余りがkになる数の個数
# 最後のans[5]が答えになる
ans = [modint(0)] * 13

for i, c in enumerate(S):
    if i == 0:
        if c != '?':
            ans[int(c)] += 1
        else:
            for q in range(10):
                ans[q] += 1
        continue

    tmp = [modint(0)] * 13

    m = mod13_of_10pow(i)
    ds = [int(c)] if c != '?' else [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for d in ds:
        for k in range(13):
            tmp[(k + d * m) % 13] += ans[k]

    ans = tmp

print(ans[5])
