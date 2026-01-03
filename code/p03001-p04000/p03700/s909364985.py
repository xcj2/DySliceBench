import sys,bisect as bs,collections as cl,heapq as hq
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

n,a,b = m()

h = []

for i in range(n):
    h.append(onem())

h.sort(reverse = True)

l = 1
r = h[0]//b+1

while l != r:
    x = (l+r)//2
    ct = 0
    for i in range(n):
        ct += ((a-b-1) + max(0,h[i]-b*x))//(a-b)
    if ct > x:
        l = x+1
    else:
        r = x
print(l)




