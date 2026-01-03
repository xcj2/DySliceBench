#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(n: int, a: "List[int]"):
    ret = []
    if n % 2 == 0:
        for i in range(n - 1, 0, -2):
            ret.append(a[i])
        for i in range(0, n - 1, 2):
            ret.append(a[i])
    else:
        for i in range(n - 1, -1, -2):
            ret.append(a[i])
        for i in range(1, n - 1, 2):
            ret.append(a[i])
    print(' '.join([str(r) for r in ret]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [ int(next(tokens)) for _ in range(n) ]  # type: "List[int]"
    solve(n, a)

if __name__ == '__main__':
    main()
