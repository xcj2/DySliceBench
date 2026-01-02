#!/usr/bin/env python3
import sys
INF = float("inf")


def f(n):
    if n & 1:
        return 3*n+1
    else:
        return n//2


def solve(s: int):
    a = [s]
    for i in range(10**7):
        s = f(s)
        # print(s)
        for av in a:
            if av == s:
                print(i+2)
                return
        a.append(s)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = int(next(tokens))  # type: int
    solve(s)


if __name__ == '__main__':
    main()
