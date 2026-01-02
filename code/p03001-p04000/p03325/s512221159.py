#!/usr/bin/env python3
import sys

def calc(n):
    ret = 0
    while n % 2 == 0:
        ret += 1
        n //= 2
    return ret

def solve(N: int, A: "List[int]"):
    ret = 0
    for a in A:
        ret += calc(a)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
