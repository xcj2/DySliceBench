#!/usr/bin/env python3
import sys
import string
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(H: int, W: int, S: "List[List[str]]"):
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'snuke':
                print(''.join(map(str, [string.ascii_uppercase[j], i+1])))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [[next(tokens) for _ in range(W)] for _ in range(H)]  # type: "List[List[str]]"
    solve(H, W, S)

if __name__ == '__main__':
    main()
