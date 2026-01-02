import sys

input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def gcd(a, b):
    if a < b:
        d, (p, q) = gcd(b, a)
        return d, (q, p)
    if b == 0:
        return a, (1, 0)
    d, (q, p) = gcd(b, a % b)
    q -= a // b * p
    return d, (p, q)


def ch(x, y):
    a1, m1 = x
    a2, m2 = y
    d, (p, q) = gcd(m1, m2)
    if (a2 - a1) % d != 0:
        return (0, -1)

    m = m1 * m2 // d
    r = (a1 + m1 * (a2 - a1) // d * p) % m
    return (r, m)


def main():
    N = int(input())
    D = len(str(N))

    res = 0
    for n in range(1, N + 1):
        p, q = int(str(n)[0]), int(str(n)[-1])
        if q == 0:
            continue
        for k in range(1, D + 1):
            if k == 1:
                res += 1 if p == q else 0
                continue

            if k == D:
                t = int(str(N)[0])
                if t < q:
                    continue
                elif t == q:
                    res += ((N - t * 10 ** (D - 1)) - p) // 10 + 1
                    continue

            res += 10 ** (k - 2)
    print(res)


if __name__ == "__main__":
    main()
