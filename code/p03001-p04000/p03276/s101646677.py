#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, K: int, x: "List[int]"):

    xneg = [0]+[xv for xv in x if xv < 0][::-1]
    xpos = [0]+[xv for xv in x if xv >= 0]

    ans = []
    # print(xneg)
    # print(xpos)
    for i in range(K+1):
        if len(xneg) <= i or len(xpos) <= K-i:
            continue
        ans.append(xpos[K-i]-2*xneg[i])
        # print(xpos[K-i], xneg[i])
    for i in range(K+1):
        if len(xpos) <= i or len(xneg) <= K-i:
            continue
        ans.append(2*xpos[i]-xneg[K-i])
        # print(xpos[i], xneg[K-i])

    # print(ans)
    print(min(ans))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, x)


if __name__ == '__main__':
    main()
