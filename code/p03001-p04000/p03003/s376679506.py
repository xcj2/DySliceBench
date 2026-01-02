import sys

def input(): return sys.stdin.readline()[:-1]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def MAT(h): return [list(map(int, input().split())) for _ in range(h)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def main():
    N, M = MAP()
    S = LIST()
    T = LIST()
    dp = [[0 for i in range(N + 1)] for j in range(M + 1)]
    for j in range(M):
        for i in range(N):
            if S[i] == T[j]:
                dp[j+1][i+1] = (dp[j][i+1] + dp[j+1][i] + 1) % mod
            else:
                dp[j+1][i+1] = (dp[j][i+1] + dp[j+1][i] - dp[j][i]) % mod
    print((dp[M][N] + 1) % mod)

if __name__ == '__main__':
    main()
