import sys,bisect as bs
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

ans = 0
w,h = m()

p = []

for i in range(w):
    k = onem()
    p.append([k,0])
for i in range(h):
    k = onem()
    p.append([k,1])
p.sort()
w,h = w+1,h+1

for i in range(len(p)):
    if p[i][1] == 0:
        ans += h*p[i][0]
        w -= 1
    else:
        ans += w * p[i][0]
        h -= 1
print(ans)
