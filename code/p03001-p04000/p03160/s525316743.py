import sys
input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
INF = 10 ** 9
N = int(input())
h = list(map(int, input().split()))
def chmin(dp, idx, b):
    if dp[idx] > b:
        dp[idx] = b
        return True
    return False
def solve(dp, i):
    if i == 0:return 0
    if dp[i] < INF: return dp[i]
    chmin(dp, i, solve(dp, i-1) + abs(h[i]-h[i-1]))
    chmin(dp, i, solve(dp, i-2) + abs(h[i]-h[i-2]))
    return dp[i]
def main():
    dp = [INF] * N
    dp[0] = 0
    dp[1] = abs(h[0]-h[1])
    print(solve(dp, N-1))
if __name__ == "__main__":
    main()