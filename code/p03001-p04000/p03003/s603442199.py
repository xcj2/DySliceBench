import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
Max = sys.maxsize
def l():
    return list(map(int,input().split()))
def m():
    return map(int,input().split())
def onem():
    return int(input())
def s(x):
    a = []
    aa = x[0]
    su = 1
    for i in range(len(x)-1):
        if aa == x[i+1]:
            a.append([aa,su])
            aa = x[i+1]
            su = 1
        else:
            su += 1
    a.append([aa,su])
    return a
def jo(x):
    return " ".join(map(str,x))

n,m = m()

S = l()
T = l()

dp = [ [0 for i in range(n+1)]  for j in range(m+1)]

for i in range(n+1):
    dp[0][i] = 1
for i in range(m+1):
    dp[i][0] = 1

for i in range(n):
    for j in range(m):
        if S[i] == T[j]:
            dp[j+1][i+1] += dp[j][i]
        dp[j+1][i+1] +=dp[j+1][i] + dp[j][i+1] - dp[j][i]
        dp[j+1][i+1] %= 10**9+7
print(dp[-1][-1])

