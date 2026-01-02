import math
from functools import lru_cache
def Frog1():
    n = int(input())
    h = list(map(int,input().split(' ')))
    @lru_cache(None)
    def Solve(i):
        if i==n-1:
            return 0
        if i==n-2:
            return abs(h[i]-h[i+1])
        return min(Solve(i+1)+abs(h[i]-h[i+1]),Solve(i+2)+abs(h[i]-h[i+2]))
    dp = [0]*n
    for i in reversed(range(n)):
        if i==n-1:
            dp[i] = 0
        elif i==n-2:
            dp[i] = abs(h[i]-h[i+1])
        else:
            dp[i] = min(dp[i+1]+abs(h[i]-h[i+1]),dp[i+2]+abs(h[i]-h[i+2]))
    print(dp[0])
def Frog2():
    n,k = input().split(' ')
    n,k = int(n),int(k)
    h = list(map(int, input().split(' ')))
    @lru_cache(None)
    def Solve(i):
        if i==n-1:
            return 0
        ans = math.inf
        for j in range(1,k+1):
            new_i = i+j
            if new_i<=n-1:
                ans = min(ans , Solve(new_i)+abs(h[i]-h[new_i]))
            else:
                break
        return ans

    dp = [0]*n
    for i in reversed(range(n)):
        if i==n-1:
            dp[i] = 0
        else:
            ans = math.inf
            for j in range(1,k+1):
                new_i = i+j
                if new_i<=n-1:
                    ans = min(ans,dp[new_i]+abs(h[i]-h[new_i]))
                else:
                    break
            dp[i] = ans
    print(dp[0])

Frog2()