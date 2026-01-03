#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def solve(n: int, m: int, x: "List[int]", y: "List[int]"):
    def make_count(n):
        nc = [0] * n
        nc[0] = nc[n - 1] = n
        for i in range(1, (n - 1) // 2 + 1):
            nc[i] = nc[n - i - 1] = (nc[i - 1] + (n - 2 * i)) % MOD
        return nc

    nc = make_count(n - 1)
    mc = make_count(m - 1)
    xs = 0
    for i in range(n - 1):
        xs += (x[i + 1] - x[i]) * nc[i]
        xs %= MOD

    ret = 0
    for j in range(m - 1):
        ret += (y[j + 1] - y[j]) * xs * mc[j]
        ret %= MOD
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    m = int(next(tokens))  # type: int
    x = [ int(next(tokens)) for _ in range(n) ]  # type: "List[int]"
    y = [ int(next(tokens)) for _ in range(m) ]  # type: "List[int]"
    solve(n, m, x, y)

if __name__ == '__main__':
    main()
