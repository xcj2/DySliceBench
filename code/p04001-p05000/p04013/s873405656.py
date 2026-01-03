#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def array(*args, initial=0):
    pre = "["*len(args)
    post = ""
    for a in args[::-1]:
        post += " for _ in range("+str(a)+")]"
    S = pre + str(initial) + post
    return eval(S)


def solve(N: int, A: int, x: "List[int]"):
    M = sum(x)
    # Nまで考慮, 使用した個数（Nまで）, 合計値
    DP = array(N+1, N+1, M+1)
    DP[0][0][0] = 1

    for i, a in enumerate(x, start=1):
        for j in range(N+1):
            for tot in range(M+1):
                DP[i][j][tot] = DP[i-1][j][tot]  # 使わない時
                if tot - a >= 0:                 # 使う時
                    DP[i][j][tot] += DP[i-1][j-1][tot-a]

    ans = 0
    for j in range(1, N+1):
        for tot in range(M+1):
            if tot / j == A:
                # if abs(tot / j-A) < 0.1:
                ans += DP[-1][j][tot]
    print(ans)
    # print(*DP[-1], sep="\n")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, x)


if __name__ == '__main__':
    main()
