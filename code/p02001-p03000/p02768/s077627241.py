def modpow(a, n, p):
    if n == 0:
        return 1
    elif n == 1:
        return a % p
    if n % 2 == 1:
        return (a * modpow(a, n-1, p)) % p
    tmp = modpow(a, n//2, p)
    return (tmp * tmp) % p


def modfactrial(a, p):
    ret = 1
    for i in range(a, 1, -1):
        ret = ret * i % p
    return ret


def main():
    mod = 10 ** 9 + 7
    n, a, b = map(int, input().split())

    # まずは繰り返し2乗法によって全部の組み合わせを求める
    # すべての組み合わせは、花を選ぶ/選ばないで組み合わせを決めれる

    ans = (modpow(2, n, mod) - 1) % mod

    # a本選んだときの数を引く
    c_a = 1
    for i in range(n, n-a, -1):
        c_a *= i
        c_a %= mod
    c_a *= modpow(modfactrial(a, mod), mod-2, mod)
    ans -= c_a
    ans %= mod

    # b本選んだときの数を引く
    c_b = 1
    for i in range(n, n-b, -1):
        c_b *= i
        c_b %= mod
    c_b *= modpow(modfactrial(b, mod), mod-2, mod)
    ans -= c_b
    ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
