import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

def main():
    N, M = LI()
    A = [0] * (N + 1)
    for _ in range(M):
        A[II()] = 1
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = dp[0] if A[1] == 0 else 0
    for i in range(2, N + 1):
        if A[i] == 1:
            dp[i] = 0
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    ans = dp[N]
    return ans

print(main())