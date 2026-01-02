#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    total = 0
    mn = float('inf')
    cnt = 0
    for a in A:
        if a < 0:
            cnt += 1
        mn = min(mn, abs(a))
        total += abs(a)
    if cnt % 2 != 0:
        total -= mn * 2
    print(total)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
