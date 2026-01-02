def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n,k = MI()
h = [0]+ LI()
#h[i]はi番目の高さ
#0-indexedにしておくと考えにくいので1-indexedにしておく
#dp[i]は足場iにいくのに必要な最小コスト
dp = [10**15]*(n+1)
#これも1-indexedにしておく
dp[1] = 0
#2番目の足場に移るのは1番目の足場からいくしかないのでわけて考える
#最初蛙は足場1にいるため最小コストは0としておく
for i in range(2,n+1):
  for j in range(1,k+1):
    if i - j >= 0:
      dp[i] = min(dp[i-j]+abs(h[i]-h[i-j]),dp[i])
print(dp[n])