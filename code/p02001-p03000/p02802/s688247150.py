#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int, p: "List[int]", S: "List[str]"):
    
    dp = [[0, 0] for i in range(N+1)]
    for i in range(M):
        if S[i] == 'AC':
            dp[p[i]][0] = 1
            
        else:
            if dp[p[i]][0] == 0:
                dp[p[i]][1] += 1

    ac = len([dp[i][0] for i in range(1, N+1) if dp[i][0] > 0])
    wa = sum([dp[i][1] for i in range(1, N+1) if dp[i][0] > 0])
    # print(dp[:10])
    # print([dp[i][0] for i in range(1, N+1)])
    print(ac, wa)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    p = [int()] * (M)  # type: "List[int]"
    S = [str()] * (M)  # type: "List[str]"
    for i in range(M):
        p[i] = int(next(tokens))
        S[i] = next(tokens)
    solve(N, M, p, S)

if __name__ == '__main__':
    main()
