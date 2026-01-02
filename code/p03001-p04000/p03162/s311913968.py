def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
n = I()
act = [[0,0,0]] + LLI(n)
dp = [[-10**10,-10**10,-10**10] for _ in range(n+1)]
#dp[i][0]はi日目でA選ぶときの幸福度の最大値
#dp[i][1]はi日目でB選ぶときの幸福度の最大値
#dp[i][2]はi日目でC選ぶときの幸福度の最大値
#1-indexedで考えよう
dp[1] = act[1]
for i in range(2,n+1):
    dp[i][0] = max(dp[i-1][1] + act[i][0], dp[i-1][2] + act[i][0])
    dp[i][1] = max(dp[i-1][0] + act[i][1], dp[i-1][2] + act[i][1])
    dp[i][2] = max(dp[i-1][1] + act[i][2], dp[i-1][0] + act[i][2])
print(max(dp[n][0],dp[n][1],dp[n][2]))
