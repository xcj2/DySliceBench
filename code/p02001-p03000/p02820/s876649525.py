#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, K: int, R: int, S: int, P: int, T: str):
    ret = 0
    a = []
    for i, c in enumerate(T):
        if c == 'r' and not (i >= K and a[i - K] == c):
            ret += P
            a.append('r')
        elif c == 's' and not (i >= K and a[i - K] == c):
            ret += R
            a.append('s')
        elif c == 'p' and not (i >= K and a[i - K] == c):
            ret += S
            a.append('p')
        else:
            a.append('g')
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    T = next(tokens)  # type: str
    solve(N, K, R, S, P, T)

if __name__ == '__main__':
    main()
