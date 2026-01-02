def pow_mod(a, b, p):
    res = 1
    mul = a
    for i in range(len(bin(b)) - 2):
        if (1 << i) & b:
            res = (res * mul) % p
        mul = (mul ** 2) % p
    return res


def comb_mod(n, r, p, factorial, invert_factorial):
    return (factorial[n] * invert_factorial[r] * invert_factorial[n - r]) % p


def main():
    p = 10 ** 9 + 7
    n, k = map(int, input().split())

    factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = (factorial[i - 1] * i) % p

    invert_factorial = [0] * (n + 1)
    invert_factorial[n] = pow_mod(factorial[n], p - 2, p)
    for i in range(n - 1, -1, -1):
        invert_factorial[i] = (invert_factorial[i + 1] * (i + 1)) % p

    res = 0
    for i in range(min(k + 1, n)):
        res = (res + comb_mod(n, i, p, factorial, invert_factorial)
               * comb_mod(n - 1, i, p, factorial, invert_factorial)) % p
    print(res)


main()
