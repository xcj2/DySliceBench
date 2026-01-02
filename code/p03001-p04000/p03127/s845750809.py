#!/usr/bin/env python3
import sys
from functools import reduce

def gcd(n, m):
    if n > m: # require n <= m
        n, m = m, n
    o = m % n
    if o == 0:
        return n
    else:
        m = n
        n = o
        return gcd(n, m)

def gcds(ns):
    return reduce(gcd, ns)

def solve(N: int, A: "List[int]"):
    """
    [思考]
    体力最小のものを Amin とおく．
    すると，試行の結果体力が Amin より小さくなる可能性がある場合はそれが答え，さもなくば Amin が答え．
    問題はその可能性をどう探索するか．
    """
    print(gcds(A))
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
