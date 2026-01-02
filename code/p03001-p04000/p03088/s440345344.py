#!/usr/bin/env python3
import sys
import numpy as np

# dp = np.ones((100, 4, 4, 4))

# tot = 0
# for x in itertools.product(*["ACGT"]*5):
#     x = "".join(x)
#     if "AGC" in x or "ACG" in x or "GAC" in x:
#         tot += 0
#     else:
#         tot += 1
# print(tot)

MOD = 1000000007  # type: int

# 例外をカウントすべきだ。
# AGCT = "AGCT"
# dp = [[0]*4 for _ in range(4) for _ in range()]
# buf = [1, 4, 16, 64]
# ans = [1, 4, 16, 61]


def solve(N: int):
    A, C, G, T = 0, 1, 2, 3
    dp = np.zeros((102, 4, 4, 4))
    dp[3] = np.ones((4, 4, 4))
    dp[3][A][G][C] = 0
    dp[3][G][A][C] = 0
    dp[3][A][C][G] = 0
    for i in range(3, N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k == A and l == G and m == C:
                            # print("AGC")
                            continue
                        elif k == G and l == A and m == C:
                            # print("GAC")
                            continue
                        elif k == A and l == C and m == G:
                            # print("ACG")
                            continue
                        elif j == A and k == G and m == C:
                            # print("AG*C")
                            continue
                        elif j == A and l == G and m == C:
                            # print("A*GC")
                            continue
                        else:
                            dp[i+1][k][l][m] += dp[i][j][k][l] % MOD
        # print(dp[i])
    print(int(np.sum(dp[N])) % MOD)
    # n = 3
    # while 1:
    #     if n == N:
    #         break
    #     dp.append(((dp[n]*4 % MOD)+(2*ans[n-2] %
    #                                 MOD)+(5*ans[n-3] % MOD)) % MOD)
    #     buf.append((buf[-1]*4) % MOD)
    #     ans.append((buf[-1]-dp[-1]) % MOD)
    #     n += 1
    # print(dp)
    # print(ans[-1])
    # print(MOD)
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
