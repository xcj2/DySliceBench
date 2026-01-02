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
    N, M = read_values()
    A = read_list()
    p = (0, 1)
    for a in A:
        p = ch((a // 2, a), p)
        if p[1] == -1:
            print(0)
            return
    print((M - p[0]) // p[1] + 1)


if __name__ == "__main__":
    main()
