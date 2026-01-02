import sys,collections as cl,bisect as bs,copy
sys.setrecursionlimit(100000)
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist 小数はfloat
    return list(map(float,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())
def s(x): #圧縮
    a = []
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

n = onem()

a = l()

dp = [[0 for i in range(n+1)]for j in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(0,n+1):
        if j == 0:
            dp[i+1][0] = dp[i][0]*(1-a[i])
        elif j == n:
            dp[i+1][-1] = dp[i][-2]*a[i]
        else:
            dp[i+1][j] = dp[i][j-1]*a[i] + dp[i][j]*(1-a[i])
    

print(sum(dp[-1][(n+1)//2:]))



