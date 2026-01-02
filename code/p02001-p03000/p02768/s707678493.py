# AtCoder用のライブラリ
# 参照
# https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a


# a ** n mod m
def mod_pow(a, n, m=10 ** 9 + 7):
    res = 1
    while n > 0:
        if n & 1 == 1:
            res = res * a % m
        a = a * a % m
        n >>= 1
    return res


# aの-1乗をmで割ったときの商を求める
def mod_inv(a, m=10 ** 9 + 7):
    b = m
    u = 1
    v = 0
    while b > 0:
        t = a // b
        a -= t * b
        c = a
        a = b
        b = c

        u -= t * v
        c = u
        u = v
        v = c
    u %= m
    return u


# 組み合わせ数(nCk)を計算させる。
# nを固定しながら複数のkに対して計算させることができるようにしてあるため、
# 計算量はO(max(k)*log(mod))のため、実質O(max(k))。
class ModCombination:
    def __init__(self, n, mod=10 ** 9 + 7):
        self.N = n
        self.MOD = mod
        self.inv_fact_list = [1]
        self.P_list = [1]

    def combination(self, r):
        if r > len(self.inv_fact_list) - 1:
            self._list_extend(r)
        return self.inv_fact_list[r] * self.P_list[r] % self.MOD

    def _list_extend(self, needed):
        now = len(self.inv_fact_list)
        while now <= needed:
            self.P_list.append(self.P_list[-1] * (self.N - now + 1) % self.MOD)
            self.inv_fact_list.append(self.inv_fact_list[-1] * mod_inv(now) % self.MOD)
            now += 1


n, a, b = map(int, input().split())

MOD = 10 ** 9 + 7

c = ModCombination(n)

ans = (mod_pow(2, n) - c.combination(b) - c.combination(a) - 1) % MOD

print(ans)