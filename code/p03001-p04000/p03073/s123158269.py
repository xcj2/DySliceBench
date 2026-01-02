#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(S: str):
    N = len(S)
    ptn1 = [1 if i & 1 else 0 for i in range(N)]
    # print(*ptn1, sep="")
    ans1 = 0
    for i, c in enumerate(S):
        if int(c) != ptn1[i]:
            ans1 += 1
    # print(ans1)
    ptn2 = [0 if i & 1 else 1 for i in range(N)]
    # print(*ptn2, sep="")
    ans2 = 0
    for i, c in enumerate(S):
        if int(c) != ptn2[i]:
            ans2 += 1
    # print(ans2)

    print(min(ans1, ans2))
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
