#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    white = []
    white.append(0)
    cur = 0
    for c in S:
        if c == '.':
            cur += 1
        white.append(cur)
    black = []
    black.append(0)
    cur = 0
    for c in S[::-1]:
        if c == '#':
            cur += 1
        black.append(cur)
    black.reverse()
    #print(white)
    #print(black)
    ret = float('inf')
    for i in range(N + 1):
        ret = min(ret, N - (white[i] + black[i]))
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
