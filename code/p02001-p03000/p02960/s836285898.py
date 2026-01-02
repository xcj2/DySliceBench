import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10 ** 9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    S = SS()

    len_S = len(S)
    dp = [[0] * 13 for _ in range(len_S + 1)]
    dp[0][0] = 1

    for i in range(len_S):
        S_i = S[i]
        for j in range(13):
            if S_i == '?':
                for k in range(10):
                    dp[i+1][(j*10+k)%13] += dp[i][j]
                    dp[i+1][(j*10+k)%13] %= MOD
            else:
                dp[i+1][(j*10+int(S_i))%13] += dp[i][j]
                dp[i+1][(j*10+int(S_i))%13] %= MOD

    # for i in dp:
    #     print(i)
    print(dp[-1][5])

if __name__ == '__main__':
    resolve()
