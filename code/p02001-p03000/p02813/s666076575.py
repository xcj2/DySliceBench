#!/usr/bin/env python3

import sys
from itertools import permutations
sys.setrecursionlimit(300000)


def solve(N: int, P: "List[int]", Q: "List[int]"):
    def equals(x, y):
        for i in range(len(x)):
            if x[i] != y[i] - 1:
                return False
        return True
    perm = list(permutations(list(range(N))))
    a = 0
    b = 0
    for i, p in enumerate(perm):
        if equals(p, P):
            a = i
        if equals(p, Q):
            b = i
    print(abs(a - b))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Q = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, Q)

if __name__ == '__main__':
    main()
