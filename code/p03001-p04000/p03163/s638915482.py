import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main(): 
    N, W = LI()
    things = []
    for i in range(N):
        things.append(LI())

    knapsack_dp = [[0 for _ in range(W+1)] for _ in range(N)]

    for i, wv in enumerate(things):  # 10**2
        w, v = wv
        if i == 0:
            for weight in range(W+1):  # 10**5
                knapsack_dp[i][weight] = 0 if weight < w else v
        else:
            for weight in range(W+1):
                if weight-w < 0:
                    knapsack_dp[i][weight] = knapsack_dp[i-1][weight]
                else:
                    knapsack_dp[i][weight] = max(knapsack_dp[i-1][weight], knapsack_dp[i-1][weight-w]+v)

    print(knapsack_dp[N-1][W])

main()