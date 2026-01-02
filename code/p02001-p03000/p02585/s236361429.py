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


n,k = m()

masc = [[0 for i in range(n+1)] for j in range(n)]
maxsu = [[0 for i in range(n+1)] for j in range(n)]

roop = [0 for i in range(n)]

p = l()

c = l()

for i in range(n):
    count = 0
    su = 0
    now = i
    for j in range(n+1):
        now = p[now] - 1
        count += 1
        su += c[now]
        masc[i][count-1] = su
        if count == 1:
            maxsu[i][count-1] = su
        else:
            maxsu[i][count-1] = max(maxsu[i][count-2],su)
        if i == now:
            roop[i] = count
            break

ans = -Max

for i in range(n):
    if k <= roop[i]:
        ans = max(ans,maxsu[i][k-1])
    else:
        if masc[i][roop[i]-1] < 0:
            ans = max(ans,maxsu[i][roop[i]-1])
        else:
            ans = max(ans,(k//roop[i]) * masc[i][roop[i]-1] + maxsu[i][k % roop[i]-1],(k//roop[i] - 1) * masc[i][roop[i]-1] + maxsu[i][roop[i]-1])
print(ans)


