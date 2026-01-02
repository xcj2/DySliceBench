def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


def divisorize(fct):
    b, e = fct.pop()  # base, exponent
    pre_div = divisorize(fct) if fct else [[]]
    suf_div = [[(b, k)] for k in range(e + 1)]
    return [pre + suf for pre in pre_div for suf in suf_div]


def num(fct):
    a = 1
    for base, exponent in fct:
        a = a * base**exponent
    return a


if __name__ == '__main__':
    # 素因数
    x, n = map(int, input().split(" "))
    r = factorize(n)
    r2 = [(c[0], c[1]//x) for c in r if c[1]>=x] # (基数, 指数)で指数をnに合わせて変換
    r3 = [c[0]**c[1] for c in r2]
    r_f = 1
    for c in r3:
        r_f *= c
    print(r_f)

    """
    # 約数列挙
    for d in divisorize(r):
        print(d, num(d))
    """
