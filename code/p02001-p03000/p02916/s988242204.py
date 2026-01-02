#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    ans = 0
    pre = -INF
    for a in A:
        ans += B[a-1]
        if pre == a-1:
            ans += C[pre-1]

        pre = a
    # 最後
    print(ans)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N - 1)]  # type: "List[int]"
    solve(N, A, B, C)


if __name__ == '__main__':
    main()
