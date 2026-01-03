MOD = 1000000007


def mod_pow(a, n, mod):
    """
    二分累乗法による a^n (mod m)の実装

    :param a: 累乗の底
    :param n: 累乗の指数
    :param mod: 法
    :return: a^n (mod m)
    """

    result = 1
    a_n = a
    while n > 0:
        if n & 1:
            result = result * a_n % mod
        a_n = a_n * a_n % mod
        n >>= 1
    return result


def mod_inverse(a, mod):
    """
    フェルマーの小定理による a^-1 ≡ 1 (mod m)の実装
    aの逆元を計算する

    a^-1 ≡ 1 (mod m)
    a * a^-2 ≡ 1 (mod m)
    a^-2 ≡ a^-1 (mod m)

    :param a: 逆元を計算したい数
    :param mod: 法
    :return: a^-1 ≡ 1 (mod m)
    """

    return mod_pow(a=a, n=mod - 2, mod=mod)


class ModCombination:
    """
    nCk (mod m)を扱うクラス
    """

    def __init__(self, mod, n_max):
        """
        イニシャライザ
        予め 1~nの階乗と階乗の逆元を計算しておく

        :param mod: 法
        :param n_max: nの最大値(100,000で約1秒)
        """
        self.mod = mod
        self.n_max = n_max
        self.facts = [1, 1]
        self.inverses = [None, 1]
        self.fact_inverses = [1, 1]

        for i in range(2, self.n_max + 1):
            self.facts.append(self.facts[i - 1] * i % self.mod)
            # self.inverses.append(mod_inverse(i, self.mod))
            self.inverses.append(self.mod - self.inverses[self.mod % i] * (
                        self.mod // i) % self.mod)
            self.fact_inverses.append(
                self.fact_inverses[i - 1] * self.inverses[i] % self.mod
            )

    def mod_combination(self, n, k):
        """
        nCk (mod m)を計算する

        :param n: n
        :param k: k
        :return: nCk (mod m)
        """
        if not 0 < k < n:
            raise ValueError

        denominator = \
            self.fact_inverses[k] * self.fact_inverses[n - k] % self.mod
        return self.facts[n] * denominator % self.mod


def calc_routes(combination, dx, dy):
    if dx == 0 or dy == 0:
        return 1
    else:
        return combination.mod_combination(dx + dy, dx)


def check(h, w, a, b):
    combination = ModCombination(mod=MOD, n_max=h + w)
    p = (b + 1, h - a)
    all_routes = 0
    while p[0] <= w and p[1] > 0:
        d1 = (p[0] - 1, p[1] - 1)
        d2 = (w - p[0], h - p[1])
        r1 = calc_routes(combination, *d1)
        r2 = calc_routes(combination, *d2)
        routes = r1 * r2 % MOD
        all_routes += routes
        all_routes %= MOD
        p = (p[0] + 1, p[1] - 1)
    return all_routes


def main():
    h, w, a, b = map(int, input().split())
    print(check(h, w, a, b))


if __name__ == '__main__':
    main()
