def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


def factorize(n):
    res = set()

    diviser = 2
    exponent = 0
    while n % diviser == 0:
        exponent += 1
        n //= diviser
    if exponent > 0:
        res.add((diviser, exponent))
    # 2の冪数を先に調べることで、
    # diviserを奇数に限定できる

    to = int(pow(n, 0.5))
    for diviser in range(3, to + 1, 2):
        exponent = 0
        while n % diviser == 0:
            exponent += 1
            n //= diviser
        if exponent > 0:
            res.add((diviser, exponent))

    if n > 1:
        res.add((n, 1))
        # n:素数の場合

    return res


def main():
    a, b = map(int, input().split())
    g = gcd(a, b)
    e = factorize(g)

    ans = len(e) + 1
    # factorizeで、素数の種類数が分かる
    # 1で割る分を +1 で加算する
    print(ans)


if __name__ == '__main__':
    main()
