
def gcd(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return gcd(b, a % b)


def solve(n, a):
    l, r = [], []
    l = [0 for i in range(n + 1)]
    r = [0 for i in range(n + 1)]
    r[n] = 0

    for i in range(0, n):
        if i == 0:
            l[0] = 0
        else:
            l[i] = gcd(l[i - 1], a[i - 1])

    for i in range(n, 0, -1):

        if i == n:
            r[i] = 0
        else:
            r[i] = gcd(r[i+1], a[i])
    m = 0
    for i in range(n):
        # print('m', m)
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
