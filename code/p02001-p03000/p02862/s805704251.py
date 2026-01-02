def mod_inverse(x, mod):
    return pow(x, mod - 2, mod)


# return nCk % mod
# it takes O(k)
def mod_comb(n, k, mod):
    numer, denom = 1, 1
    for i in range(k):
        numer = numer * ((n - i) % mod) % mod
        denom = denom * ((i + 1) % mod) % mod

    return numer * mod_inverse(denom, mod) % mod


def main():
    mod = 10**9 + 7
    X, Y = map(int, input().split())

    t1, t2 = 2 * Y - X, 2 * X - Y
    if t1 % 3 != 0 or t2 % 3 != 0 or t1 < 0 or t2 < 0:
        print(0)
        return

    a, b = t1 // 3, t2 // 3
    print(mod_comb(a + b, a, mod))


main()