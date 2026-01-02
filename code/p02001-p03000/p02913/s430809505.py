import sys
import heapq
import bisect

mod = 10**9+7
dd = ((-1,0),(1,0),(0,-1),(0,1))

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return(list(sys.stdin.readline())[:-1])

def main():
    N = I()
    s = S()
    dp = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            if s[i] == s[j]:
                if i+1<=N-1 and j+1<=N-1:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = 1

    ans = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] > ans and i + dp[i][j] <= j:
                ans = dp[i][j]
    return(ans)

if __name__ == "__main__":
    print(main())
