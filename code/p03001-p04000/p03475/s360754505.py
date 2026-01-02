#!/usr/bin/env python3
import sys


def solve(N: int, C: "List[int]", S: "List[int]", F: "List[int]"):
    ret = []
    for i in range(N - 1):
        tmp = 1
        for j in range(i, N - 1):
            if tmp > S[j]:
                tmp = ((tmp - S[j] - 1) // F[j] + 1) * F[j] + S[j] + C[j]
            else:
                tmp = S[j] + C[j]
        ret.append(tmp)
    ret.append(0)
    for r in ret:
        print(r)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [int()] * (N-1)  # type: "List[int]" 
    S = [int()] * (N-1)  # type: "List[int]" 
    F = [int()] * (N-1)  # type: "List[int]" 
    for i in range(N-1):
        C[i] = int(next(tokens))
        S[i] = int(next(tokens))
        F[i] = int(next(tokens))
    solve(N, C, S, F)

if __name__ == '__main__':
    main()
