import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    n, m = map(int, input().split())
    # https://atcoder.jp/contests/abc156/submissions/11621672
    def modpow(a, b, mod=10 ** 9 + 7):
        ret = 1
        while b > 0:
            if b % 2 == 1:
                ret = ret * a % mod
            a = a * a % mod
            b //= 2
        return ret


    def modcomb(n, c, mod=10 ** 9 + 7):
        if n<c:
            return 0
        if c > n - c:
            c = n - c
        u, d = 1, 1
        for i in range(c):
            u = u * (n - i) % mod
            d = d * (i + 1) % mod
        return u * modpow(d, mod - 2) % mod


    """mod = 10 ** 9 + 7
    n, a, b = map(int, input().split())
    ans = (modpow(2, n) - 1) % mod
    ans = (ans-modcomb(n, a)) % mod
    ans = (ans-modcomb(n, b)) % mod
    print(ans)"""

    # combどうしの積をとると余りがずれるので避ける！　普通のcombを計算して最後にmodをとって。

    import math

    # cf. https://qiita.com/suecharo/items/14137fb74c26e2388f1f
    def make_prime_list_2(num):
        if num < 2:
            return []

        # 0のものは素数じゃないとする
        prime_list = [i for i in range(num + 1)]
        prime_list[1] = 0  # 1は素数ではない
        num_sqrt = math.sqrt(num)

        for prime in prime_list:
            if prime == 0:
                continue
            if prime > num_sqrt:
                break

            for non_prime in range(2 * prime, num, prime):
                prime_list[non_prime] = 0

        return [prime for prime in prime_list if prime != 0]

    def prime_factorization_2(num):
        """numの素因数分解
        素因数をkeyに乗数をvalueに格納した辞書型dict_counterを返す"""

        if num == 1:
            return False
        else:
            num_sqrt = math.floor(math.sqrt(num))
            prime_list = make_prime_list_2(num_sqrt)

            dict_counter = {}  # 何度もこの関数を呼び出して辞書を更新したい時はこれを引数にして
            # cf. https://atcoder.jp/contests/arc034/submissions/12251452

            for prime in prime_list:
                while num % prime == 0:
                    if prime in dict_counter:
                        dict_counter[prime] += 1
                    else:
                        dict_counter[prime] = 1
                    num //= prime
            if num != 1:
                if num in dict_counter:
                    dict_counter[num] += 1
                else:
                    dict_counter[num] = 1

            return dict_counter

    ans = 1
    if not prime_factorization_2(m):
        print(1)
    else:
        d = prime_factorization_2(m)
        mod = 10 ** 9 + 7

        for k, v in d.items():
            ans = ans * modcomb(v + n - 1, n - 1)
        print(ans % mod)


resolve()