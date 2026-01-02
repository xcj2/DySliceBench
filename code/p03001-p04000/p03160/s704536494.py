import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    N = int(readline())
    H = [int(i) for i in readline().split()]
    INF = int(1e9)
    #dp[i]:= 足場iまでの最小コスト
    dp = [INF for _ in range(N)]
    dp[0] = 0
    def f1(i):
        if i-1 < 0:
            return INF
        return dp[i-1]+abs(H[i]-H[i-1])

    def f2(i):
        if i-2 < 0:
            return INF
        return dp[i-2]+abs(H[i]-H[i-2])

    for i in range(N):
        dp[i] = min(dp[i], f1(i))
        dp[i] = min(dp[i], f2(i))

    print(dp[N-1])
if __name__ == '__main__':
    main()
