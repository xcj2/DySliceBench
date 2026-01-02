#!/usr/bin/env python3
import sys


def solve(n: int, p: "List[int]"):
    count = 0
    for i in range(1, n-1):
        if p[i-1] <= p[i] and p[i] <= p[i+1]:
            count += 1
        elif p[i+1] <=p[i] and p[i] <= p[i-1]:
            count += 1
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    p = [ int(next(tokens)) for _ in range(n) ]  # type: "List[int]"
    solve(n, p)

if __name__ == '__main__':
    main()
