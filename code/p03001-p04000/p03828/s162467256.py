#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def solve(N: int):
    elms = [0] * (N + 1)
    for i in range(2, N + 1):
        tmp = i
        j = 2
        while j <= i:
            while tmp % j == 0:
                elms[j] += 1
                tmp //= j
            j += 1
    ret = 1
    for e in elms:
        if e > 0:
            ret *= e + 1
            ret %= MOD
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
