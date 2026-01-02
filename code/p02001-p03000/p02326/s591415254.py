import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    H, W = LI()
    c = [LI() for _ in range(H)]

    # dp[i][j]: (i-1, j-1)から左上に作れる最大正方形の1辺の長さ
    dp = [[0] * (W + 1) for _ in range(H + 1)]

    max_len = 0
    for i in range(H):
        for j in range(W):
            if c[i][j] == 1:
                dp[i+1][j+1] = 0
            else:
                dp[i+1][j+1] = min(dp[i][j+1], dp[i][j], dp[i+1][j]) + 1
            max_len = max(dp[i+1][j+1], max_len)

    print(max_len ** 2)

    # for i in dp:
    #     print(i)

if __name__ == '__main__':
    resolve()

