def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve(n, a):
    l = [0] * n
    r = [0] * (n + 1)

    for i in range(1, n):
        l[i] = gcd(l[i - 1], a[i - 1])
    for i in range(n - 1, 0, -1):
        r[i] = gcd(r[i + 1], a[i])

    m = 0
    for i in range(n):
        m = max(m, gcd(l[i], r[i + 1]))
    return m


def input_from_console():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a


def main():
    n, a_list = input_from_console()
    print(solve(n, a_list))


if __name__ == "__main__":
    main()
