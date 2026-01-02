import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def YesNo(x): return 'Yes' if x else 'No'
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

def main():
    N, M = LI()
    S = LI()
    T = LI()
    dp = [[1] * (M + 1)] + [[1] + [0] * M for _ in range(N)]
    for j in range(1, 1 + N):
        for i in range(1, 1 + M):
            if S[j - 1] == T[i - 1]:
                dp[j][i] = (dp[j][i - 1] + dp[j - 1][i]) % MOD
            else:
                dp[j][i] = (dp[j][i - 1] + dp[j - 1][i] - dp[j - 1][i - 1]) % MOD
    ans = dp[-1][-1]
    return ans

print(main())