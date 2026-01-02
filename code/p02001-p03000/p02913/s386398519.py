import sys,collections as cl,bisect as bs , heapq as hq
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
    if k != len(a) and a[k][0] ==  x:
        return True
    else:
        return False

def search(a,n):
    se = dict()
    for i in range(0,len(a)-n+1):
        kkk = a[i:i+n]
        kkk = "".join(kkk)
        if kkk in se:
            if se[kkk] <= i-n:
                    return True
        else:
            se[kkk] = i
    return False


n = onem()

s = list(input())
l = 0
r = n//2
while True:
    mid = -(-(l+r)//2)
    ans = search(s,mid)
    if l == mid:
        break
    if ans:
        l = mid
    else:
        r = mid-1
print(l)
