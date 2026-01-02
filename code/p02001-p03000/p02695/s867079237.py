#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)
from itertools import combinations, combinations_with_replacement


#def solve(N: int, M: int, Q: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]"):
def solve(n, m, Q, a, b, c, d, X):
    cans = list(combinations_with_replacement(range(1, m + 1), n))
    #print(cans)
    ret = 0
    for can in cans:
        tmp = 0
        for i in range(Q):
            if can[b[i] - 1] - can[a[i] - 1] == c[i]:
                tmp += d[i]
        ret = max(tmp, ret)
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int()] * (Q)  # type: "List[int]"
    b = [int()] * (Q)  # type: "List[int]"
    c = [int()] * (Q)  # type: "List[int]"
    d = [int()] * (Q)  # type: "List[int]"
    X = []
    for i in range(Q):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
        X.append((a[i], b[i], c[i], d[i]))
    solve(N, M, Q, a, b, c, d, X)

if __name__ == '__main__':
    main()
