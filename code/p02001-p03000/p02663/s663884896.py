#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(H: "List[int]", M: "List[int]", K: int):
    s = H[0] * 60 + M[0]
    t = H[1] * 60 + M[1]
    ret = t - s - K
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = [int()] * (2)  # type: "List[int]"
    M = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        H[i] = int(next(tokens))
        M[i] = int(next(tokens))
    K = int(next(tokens))  # type: int
    solve(H, M, K)

if __name__ == '__main__':
    main()
