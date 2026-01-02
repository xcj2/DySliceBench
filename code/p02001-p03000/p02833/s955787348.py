#!/usr/bin/env python3
import sys
INF = float("inf")


def f(n):
    ans = 1
    while True:
        if n < 2:
            break
        ans *= n
        n -= 2
    return ans


def solve(N: int):
    if N % 2 == 1:
        print(0)
        return

    # a = f(15)
    # print(a)
    # print("個数: ", str(a).count("0"))

    # a = f(150)
    # print(a)
    # print("個数: ", str(a).count("0"))

    # a = f(150)
    # print(a)
    # print("個数: ", str(a).count("0"))
    # ans = 0
    # n = N
    # while True:
    #     n //= 10
    #     ans += n
    #     if n < 10:
    #         break
    # print(ans)

    tot = 0
    base = 5
    while base <= N:
        tot += (N//base)//2
        base *= 5
    print(tot)

    # tot2 = 0
    # base = 10
    # while base <= N:
    #     tot2 += N//base
    #     base *= 10
    # print(tot-tot2)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
