#!/usr/bin/env python3
import sys
MOD = 998244353  # type: int

def solve(N: int, S: int, A: "List[int]"):
    dp = [[0]*(S+1) for _ in range(N+1)]

    for i in range(N):
        for s in range(S+1):
            if s >= A[i]:
                dp[i+1][s] = dp[i][s]+dp[i][s-A[i]]+int(A[i]==s or s==0)
            else:
                dp[i+1][s] = dp[i][s]+int(A[i]==s or s==0)
            dp[i+1][s]%=MOD
    
    answer = 0
    for i in range(N):
        answer += dp[i+1][S]
    print(answer%MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, S, A)

if __name__ == '__main__':
    main()
