#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int):
    def dig(n):
        ret = 0
        while n > 0:
            ret += 1
            n //= 10
        return ret
    ret = 0
    for i in range(1, N + 1):
        if dig(i) % 2 == 1:
            ret += 1
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
