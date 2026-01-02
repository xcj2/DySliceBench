#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, B: "List[int]"):
    ans = B[-1]
    pre = 0
    for i in range(N-2, 0, -1):
        ans += min(B[i], B[i-1])
    ans += B[0]
    print(ans)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    B = [int(next(tokens)) for _ in range(N - 1)]  # type: "List[int]"
    solve(N, B)


if __name__ == '__main__':
    main()
