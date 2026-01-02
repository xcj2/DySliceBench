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

p = [0] + l() + [n+1]
ans = 0
a = [0 for i in range(n+2)]

for i in range(n+2):
    a[p[i]] = i
l1 = [max(0,i-1) for i in range(n+2)]
l2 = [max(0,i-2) for i in range(n+2)]
r1 = [min(n+1,i+1) for i in range(n+2)]
r2 = [min(n+1,i+2) for i in range(n+2)]


for i in range(n+1):
    m = a[i]
    x2,x1,y1,y2 = l2[m],l1[m],r1[m],r2[m]
    hoge= i*(abs((m-x1)*(y2-y1)) + abs((y1-m)*(x1-x2)))
    ans += hoge
    #x1
    r1[x1] = y1
    r2[x1] = y2
    #y1
    l1[y1] = x1
    l2[y1] = x2
    #x2
    r1[x2] = x1
    r2[x2] = y1
    #y2
    l1[y2] = y1
    l2[y2] = x1
print(ans)


