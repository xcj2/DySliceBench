#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(S: str):
    N = len(S)
    ans = [0]*N
    curr = 0
    while curr < N:
        counter = [0, 0]
        while S[curr] == "R":
            counter[curr % 2] += 1
            curr += 1
        R, L = curr-1, curr
        RL = [(curr-1) % 2, curr % 2]
        while curr < N and S[curr] == "L":
            counter[curr % 2] += 1
            curr += 1
        # print(R, L, counter)
        ans[R] = counter[RL[0]]
        ans[L] = counter[RL[1]]
    print(*ans, sep=" ")

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == '__main__':
    main()
