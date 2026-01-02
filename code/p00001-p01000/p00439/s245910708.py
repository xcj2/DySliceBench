#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h(typ) if m > 1 else typ(input()) for _ in range(n)]


def solve():
    n, k = read_h()
    arr = read_v(n)

    cumul = [sum(arr[:i]) for i in range(len(arr) + 1)]
    #  print(cumul)

    ans = 0
    for i in range(n - k + 1):
        s = cumul[i + k] - cumul[i]
        ans = max(ans, s)

    print(ans)


def main():
    while True:
        n, k = read_h()
        if (n, k) == (0, 0):
            break

        arr = read_v(n)

        cumul = [0]
        for i in range(n):
            cumul.append(cumul[i] + arr[i])

        ans = 0
        for i in range(n - k + 1):
            s = cumul[i + k] - cumul[i]
            ans = max(ans, s)

        print(ans)


if __name__ == '__main__':
    main()

