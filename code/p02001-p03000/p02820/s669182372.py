#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, K: int, R: int, S: int, P: int, T: str):
    score = [R, S, P]

    ans = 0
    past = []
    for i, t in enumerate(T):
        if t == "r":
            cand = 2
        elif t == "s":
            cand = 0
        else:
            cand = 1
        if i - K >= 0 and past[i-K] == cand:
            ans += 0
            past.append(-1)
        else:
            ans += score[cand]
            past.append(cand)
    print(ans)
    # print(past)

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
