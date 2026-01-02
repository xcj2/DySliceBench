#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(X: int, K: int, D: int):
    X = abs(X)
    mx = K * D
    tmp = X % D
    #print(mx, tmp, X - tmp)
    if mx < X - tmp:
        ret = X - mx
    elif (X - tmp) // D == K:
        ret = tmp
    else:
        d = X - tmp
        n = d // D
        if n % 2 == K % 2:
            ret = tmp
        else:
            ret = abs(tmp - D)
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(X, K, D)

if __name__ == '__main__':
    main()
