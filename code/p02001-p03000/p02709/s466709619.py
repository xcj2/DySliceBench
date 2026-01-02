import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())
def s(x): #圧縮
    a = []
    if len(x) == 0:
        return []
    aa = x[0]
    su = 1
    for i in range(len(x)-1):
        if aa != x[i+1]:
            a.append([aa,su])
            aa = x[i+1]
            su = 1
        else:
            su += 1
    a.append([aa,su])
    return a
def jo(x): #listをスペースごとに分ける
    return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False

def pow_k(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

"""
def nibu(x,n,r):
    ll = 0
    rr = r
    while True:
        mid = (ll+rr)//2

    if rr == mid:
        return ll
    if (ここに評価入れる):
        rr = mid
    else:
        ll = mid+1
"""

n = onem()

a = l()

aa = [[a[i],i] for i in range(n)]

aa.sort(reverse = True)

dp = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(1,n+1):
    on = aa[i-1]
    for j in range(i+1):
        if j-1 >= 0:
            dp[i-j][j] = max(dp[i-j][j-1] + on[0] * abs(on[1] - (n-1 - (j - 1))),dp[i-j][j])
            """
            if i == 1:
                print(dp[i-j][j-1] + on[0] * abs(on[1] - j),dp[i-j][j])
            """
        if i-j-1 >= 0:
            #dp[i-j][j] = max(dp[i-j][j],dp[i-j-1][j] + on[0] * abs(on[1] - (n-1 - (i-j))))
            dp[i-j][j] = max(dp[i-j][j],dp[i-j-1][j] + on[0] * abs(on[1] - (i-j-1)))
            """
            if i == 1:
                print(on,(n-1 - (i-j)),n-1,i-j)
                print(dp[i-j-1][j],on[0] * abs(on[1] - (n-1 - (i-j))))
                print(dp[i-j][j],dp[i-j-1][j] + on[0] * abs(on[1] - (i-j-1)))
            """

ma = 0    
for i in range(n+1):
    ma = max(ma,dp[n-i][i])
print(ma)





