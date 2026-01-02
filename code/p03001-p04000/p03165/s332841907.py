#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(S: str, T: str):
    lenS, lenT = len(S), len(T)
    DP = [[0]*(lenT+1) for _ in range(lenS+1)]
    for i in range(lenS):
        for j in range(lenT):
            if S[i] == T[j]:
                DP[i+1][j+1] = max(DP[i][j]+1, DP[i+1][j+1])
            DP[i+1][j+1] = max(DP[i+1][j], DP[i][j+1], DP[i+1][j+1])

    ans = ""
    i, j = lenS, lenT
    while i > 0 and j > 0:
        if DP[i][j] == DP[i-1][j]:
            i -= 1
        elif DP[i][j] == DP[i][j-1]:
            j -= 1
        else:
            ans = S[i-1] + ans
            i -= 1
            j -= 1
    print(ans)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    t = next(tokens)  # type: str
    solve(s, t)


if __name__ == '__main__':
    main()
