#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, S: str):
    x = 0
    anx = 0
    for i in range(N):
        if S[i] == 'I':
            x += 1
        else:
            x -= 1
        anx = max(anx, x)

    print(anx)

    
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
