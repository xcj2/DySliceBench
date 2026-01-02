#!/usr/bin/env python3
import sys


def solve(N: int, K: int, R: int, S: int, P: int, T: str):
    memo = [""]*N

    for i in range(N):
        t = T[i]
        if t == "r":
            if i < K:
                memo[i] = "p" 
            else:
                if memo[i-K] == "p":
                    memo[i] = "."
                else:
                    memo[i] = "p"

        elif t == "s":
            if i < K:
                memo[i] = "r" 
            else:
                if memo[i-K] == "r":
                    memo[i] = "."
                else:
                    memo[i] = "r"
        else:
            if i < K:
                memo[i] = "s" 
            else:
                if memo[i-K] == "s":
                    memo[i] = "."
                else:
                    memo[i] = "s"
    score = 0

    for i in range(N):
        if memo[i] == "p":
            score+=P
        elif memo[i] == "s":
            score += S
        elif memo[i] == "r":
            score += R
        else:
            continue
    
    print(score)
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
