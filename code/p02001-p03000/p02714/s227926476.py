#!/usr/bin/env python3
import sys
from collections import Counter
sys.setrecursionlimit(10**8)
INF = float("inf")


def solve(N: int, S: str):
    c = Counter(S)
    count = c["R"] * c["G"]*c["B"]
    for i in range(1, (N-3)//2+2):
        for j in range(N):
            if j+2*i >= N:
                break
            if not (S[j] == S[j+i] or S[j] == S[j+i+i] or S[j+i] == S[j+i+i]):
                count -= 1
    print(count)

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
