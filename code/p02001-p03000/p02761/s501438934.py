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
    return "".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False
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

N,M = m()

a = [-1 for i in range(N)]

for i in range(M):
    s,c = m()
    s -= 1
    if a[s] == -1 or a[s] == c:
        a[s] = c
    else:
        print(-1)
        exit()
for i in range(N):
    if i == 0:
        if a[i] == 0 and N != 1:
            print(-1)
            exit()
        elif a[i] == 0:
            break
        elif a[i] == -1 and N != 1:
            a[i] = 1
        elif a[i] == -1:
            a[i] = 0
    else:
        if a[i] == -1:
            a[i] = 0

print(jo(a))


