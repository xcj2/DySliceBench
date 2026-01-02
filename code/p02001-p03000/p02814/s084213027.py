def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    from math import ceil

    n, m, *a = map(int, open(0).read().split())
    c = 0
    t = a[0]
    while t % 2 == 0:
        c += 1
        t = t // 2

    for x in a[1:]:
        d = 0
        while x % 2 == 0:
            d += 1
            x = x // 2

        if d != c:
            print(0)
            break

        t = lcm(t, x)
    else:
        ans = ceil(m // 2 ** (c-1) // t / 2)
        print(ans)


if __name__ == "__main__":
    main()
