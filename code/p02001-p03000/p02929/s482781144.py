#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def solve(N: int, S: str):
    tmp = 0
    p = 1
    for c in S:
        if c == 'B':
            if tmp % 2 == 0:
                tmp += 1
            elif tmp > 0:
                p *= tmp
                p %= MOD
                tmp -= 1
            else:
                print(0)
                return
        if c == 'W':
            if tmp % 2 == 1:
                tmp += 1
            elif tmp > 0:
                p *= tmp
                p %= MOD
                tmp -= 1
            else:
                print(0)
                return
    if tmp > 0:
        print(0)
        return

    ret = 1
    for i in range(1, N + 1):
        ret *= i
        ret %= MOD
    ret *= p
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
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
