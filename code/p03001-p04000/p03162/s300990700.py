def i():
	return int(input())
def i2():
	return map(int,input().split())
def s():
	return str(input())
def l():
	return list(input())
def intl():
	return list(int(k) for k in input().split())

n = i()
h = [intl() for _ in range(n)]

dp = [[0]*3 for _ in range(n)]
for i in range(n):
    if i == 0:
        dp[i][0] = h[i][0]
        dp[i][1] = h[i][1]
        dp[i][2] = h[i][2]
    else:
        for j in range(3):
           dp[i][0] = max( dp[i-1][1] + h[i][0], dp[i-1][2] + h[i][0] )
           dp[i][1] = max( dp[i-1][0] + h[i][1], dp[i-1][2] + h[i][1] )
           dp[i][2] = max( dp[i-1][0] + h[i][2], dp[i-1][1] + h[i][2] )
print( max(dp[n-1]) )