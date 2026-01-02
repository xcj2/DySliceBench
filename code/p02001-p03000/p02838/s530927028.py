import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
mod = 10**9+7
Max = sys.maxsize
input = sys.stdin.readline
def l(): #intのlist
    return list(map(int,input().split()))
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


def ans():
    n = onem()

    a = l()

    dp = [[0]*60 for j in range(n+1)]

    co = 0

    for i in range(1,n+1):
        kkk = a[i-1]
        for j in range(60):
            if j != 0:
                kkk = kkk // 2
            if kkk & 1:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = dp[i-1][j]

    two = [0 for i in range(61)]
    two[0] = 1
    for i in range(1,61):
        two[i] = (two[i-1]*2) % mod
        

    for i in range(1,n):
        for j in range(60):
            if dp[i][j] == dp[i-1][j]:
                ans = two[j]*(dp[-1][j]-dp[i][j])
                ans %= mod
                co += ans
                co %= mod
            else:
                ans = two[j]*(n-(i-1) - (dp[-1][j] - dp[i-1][j]))
                ans %= mod
                co += ans
                co %= mod

    print(co)

if __name__ == '__main__':
    ans()





