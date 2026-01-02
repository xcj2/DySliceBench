import sys
sys.setrecursionlimit(10 ** 7)
read = sys.stdin.buffer.read 
inp = sys.stdin.buffer.readline
def inpS(): return inp().rstrip().decode()
readlines = sys.stdin.buffer.readlines 
MOD = 10**9+7


def resolve():
    def dfs(l, r):
        if r - l == 1:
            dp[l][r] = A[l] + A[r]
            return dp[l][r]

        if dp[l][r] is not None:
            return dp[l][r]

        ret = 1<<60
        for x in range(l,r):
            cost = cum_A[r+1] - cum_A[l]
            ret = min(ret, dfs(l, x) + dfs(x+1, r) + cost)

        dp[l][r] = ret
        return ret

    N = int(input())
    A = list(map(int, input().split()))
    cum_A = [0]*(N+1)
    for i in range(N):
        cum_A[i+1] = cum_A[i] + A[i]

    dp = [[None]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][i] = 0

    return print(dfs(0, N-1))

if __name__ == "__main__":
    resolve()