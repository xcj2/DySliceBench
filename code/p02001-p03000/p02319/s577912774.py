import sys, bisect
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, W = LI()
    vw = [LI() for _ in range(N)]

    v_sum = sum([i[0] for i in vw])

    # dp[i][j]: [0, i)を使って価値j以上になる場合の重さの最小値
    dp = [[INF] * (v_sum + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 0

    for i in range(N):
        for j in range(v_sum):
            v_p = max(j + 1 - vw[i][0], 0)
            if v_p >= 0:
                dp[i+1][j+1] = min(dp[i][j+1], dp[i][v_p] + vw[i][1])
            else:
                dp[i+1][j+1] = dp[i][j+1]

    # for i in dp:
    #     print(i)
    
    ans = bisect.bisect_right(dp[-1], W) - 1
    print(ans)

if __name__ == '__main__':
    resolve()
