#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(n: int):
    def is_valid(i, j, k, l):
        if ((j == 0 and k == 1 and l == 2) or
            (j == 0 and k == 2 and l == 1) or
            (j == 2 and k == 0 and l == 1) or
            (i == 0 and k == 2 and l == 1) or
            (i == 0 and j == 2 and l == 1)):
            return False
        return True
    dp = [[[1] * 4 for _ in range(4)] for _ in range(4)]
    dp[0][1][2] = 0
    dp[0][2][1] = 0
    dp[2][0][1] = 0
    for i in range(3, n):
        next_dp = [[[0] * 4 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if is_valid(i, j, k, l):
                            next_dp[j][k][l] += dp[i][j][k]
        dp = next_dp
    ret = sum([sum([sum(e) for e in d ]) for d in dp]) % MOD

    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
