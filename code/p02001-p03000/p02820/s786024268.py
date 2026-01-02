import sys
def I(): return int(sys.stdin.readline())
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N,K = LI()
R,S,P = LI()
T = list(input())
dp = [[0]*3 for _ in range(N+1)]

def main():
    for i in range(1,N+1):
        if i<K:
            if T[i-1] == 's':
                dp[i] = [R,0,0]
            if T[i-1] == 'p':
                dp[i] = [0,S,0]
            if T[i-1] == 'r':
                dp[i] = [0,0,P]
        else:
            dp[i][0] = max(dp[i-K][1],dp[i-K][2])
            dp[i][1] = max(dp[i-K][0],dp[i-K][2])
            dp[i][2] = max(dp[i-K][0],dp[i-K][1])
            if T[i-1] == 's':
                dp[i][0] += R
            if T[i-1] == 'p':
                dp[i][1] += S
            if T[i-1] == 'r':
                dp[i][2] += P
    ans = 0
    for i in range(K):
        ans += max(dp[N-i])
    print(ans)


if __name__ == "__main__":
    main()
