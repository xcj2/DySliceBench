#!/usr/bin/env python3
import sys


def solve(N: int):
    ret = 0
    i = 1
    used = set()
    while (i - 1) ** 2 <= N:
        #print(i)
        tmp = N - i
        if tmp % i == 0:
            val = tmp // i
            if val > 0 and N // val == N % val and not val in used:
                ret += val
                used.add(val)
        if N % (i + 1):
            val = N // (i + 1) != i
            if val > 0 and N // val == N % val and not val in used:
                ret += val
                used.add(val)
        i += 1
    print(ret)
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
