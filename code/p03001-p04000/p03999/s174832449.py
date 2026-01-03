#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(S: str):
    DP = [0]*(len(S)+1)

    for i in range(len(S)):
        # print("-")
        DP[i+1] = DP[0] + int(S[:i+1])
        # print(DP[0] + int(S[i]))
        for j in range(i):
            DP[i+1] += DP[j+1]+int(S[j+1:i+1])*(2**j)
            # print(DP[j+1]+int(S[j+1:i+1])*(2**j))
    print(DP[-1])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = str(next(tokens))  # type: int
    solve(S)


if __name__ == '__main__':
    main()
