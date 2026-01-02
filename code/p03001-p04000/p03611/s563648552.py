#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    counts = [0] * 100000
    a.sort()
    for v in a:
        counts[v] += 1
    ret = 0
    for i in range(len(counts) - 2):
        ret = max(ret, counts[i] + counts[i + 1] + counts[i + 2])
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
