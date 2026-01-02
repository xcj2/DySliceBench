import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
def LILI(n): return [LI() for _ in range(n)]
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main(): 
    N = II()
    p = LF()

    # dp[これまでに表が出た数][コインの番号], 中身は確率
    dp = [[0.0 for _ in range(N+1)] for _ in range(N)]
    dp[0][0] = 1 - p[0]
    dp[0][1] = p[0]

    for i, pos in enumerate(p[1:]):
        for j in range(i+2):
            dp[i+1][j] += dp[i][j]*(1-pos)
            dp[i+1][j+1] += dp[i][j]*pos

    ans = sum(dp[N-1][N//2+1:])

    print(ans)

main()