import sys,bisect as bs,collections as cl
sys.setrecursionlimit(100000)
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

ans = 0
a = []

for i in range(n):
    a.append(l())

for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][j] > a[i][k] + a[k][j]:
                print(-1)
                exit()
for i in range(n-1):
    for j in range(i,n):
        for k in range(n):
            if i == k or k == j:
                continue
            if a[i][j] == a[i][k] + a[k][j]:
                break
        else:
            ans += a[i][j]
    

print(ans)


