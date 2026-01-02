from sys import stdin
##  input functions for me
def ria(sep = ''):
    if sep == '' :
        return list(map(int, input().split())) 
    else: return list(map(int, input().split(sep)))
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##

## main ##
N = ri()
A = ria()
inf = int(1e18)

dp = [0] * 2
dp[0] = [-inf] * (N + 1)
dp[1] = [-inf] * (N + 1)

dp[0][1] = A[0]
dp[1][1] = - A[0]
for i in range(1, N - 1):
    dp[0][i + 1] = max(dp[0][i + 1], dp[0][i] + A[i])
    dp[1][i + 1] = max(dp[1][i + 1], dp[0][i] - A[i])
    dp[0][i + 1] = max(dp[0][i + 1], dp[1][i] - A[i])
    dp[1][i + 1] = max(dp[1][i + 1], dp[1][i] + A[i])

ma = max(dp[0][N - 1] + A[N - 1], dp[1][N - 1] - A[N - 1])

print(ma)


