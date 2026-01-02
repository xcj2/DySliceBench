#!/usr/bin/env python3
import sys
INF = float("inf")


def cmb(n, r):
    r = min(r, n-r)
    if r == 0:
        return 1
    if r == 1:
        return n

    numer = [n - r + k + 1 for k in range(r)]
    denom = [k + 1 for k in range(r)]

    for p in range(2, r+1):
        pivot = denom[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numer[k - offset] /= pivot
                denom[k] /= pivot

    result = 1
    for k in range(r):
        if numer[k] > 1:
            result *= int(numer[k])

    return result


def solve(N: int, K: int):

    # N以下のKの倍数の個数
    ans = (N//K)**3
    # print(ans)

    if K & 1 == 0:
        # 偶数ならK//2の倍数であってKの倍数でないものの組み合わせも必要
        ans += (N//(K//2) - N//K)**3

    print(ans)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)


if __name__ == '__main__':
    main()
