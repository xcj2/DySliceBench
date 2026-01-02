import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def egcd(a: int, b: int):
    """extended gcd"""
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def mod_inv(a, mod=10**9 + 7):
    """mod inversion """
    g, x, y = egcd(a, mod)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % mod


def mod_combination(n, r, mod=10**9 + 7) -> int:
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) * mod_inv(i + 1, mod) % mod
    return res


def main():
    MOD = 10**9 + 7
    n, k = input_int_list()
    for i in range(1, k + 1):
        # 青を仕切る赤が足りない場合
        if i > n - k + 1:
            print(0)
        else:
            # 青を分割するパターン
            div_pat = mod_combination(k - 1, i - 1)
            # 残った赤を配置するパターン
            rem = n - k - (i - 1)
            red_pat = mod_combination(rem + i, rem)
            cnt = (div_pat * red_pat) % MOD
            print(cnt)
    return


if __name__ == "__main__":
    main()
