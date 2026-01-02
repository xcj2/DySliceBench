#!/usr/bin/env python3
import sys
input = lambda: sys.stdin.readline().strip()

def solve(N: int, M: int, p: "List[int]", S: "List[str]"):
    solved = [False for i in range(N + 1)]
    penalties = [0 for i in range(N + 1)]
    for prob, verd in zip(p, S):
        if not solved[prob]:
            penalties[prob] += verd == 'WA'
            solved[prob] = verd == 'AC'
    print(sum(solved), sum(penalty for i, penalty in enumerate(penalties) if solved[i]))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    p = [int()] * (M)  # type: "List[int]"
    S = [str()] * (M)  # type: "List[str]"
    for i in range(M):
        p[i] = int(next(tokens))
        S[i] = next(tokens)
    solve(N, M, p, S)

if __name__ == '__main__':
    main()
