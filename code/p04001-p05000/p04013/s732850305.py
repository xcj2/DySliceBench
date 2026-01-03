#!/usr/bin/env python3
import sys
# dp[j][t]=(y1,...,yj から 0 枚以上選んで yi の合計を t − 1250 にするような選び方の総数)

def solve(N: int, A: int, x: "List[int]"):
    x = [x[i]-A for i in range(N)]
    dp = [[0]*2500 for _ in range(N+1)]
    dp[0][1250] = 1

    for j in range(1,N+1):
        for t in range(2500):
            if t-x[j-1]>=0 and t-x[j-1]<2500:
                dp[j][t] = dp[j-1][t] + dp[j-1][t-x[j-1]]
            else:
                dp[j][t] = dp[j-1][t]
    print(dp[N][1250]-1)
    
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
