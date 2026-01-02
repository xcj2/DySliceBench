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

p = l()

p.sort(reverse = True)

ms = p[0]
s = [p[0]]

for i in range(n):
    count = 0
    local = 0
    s.sort(reverse = True)
    while count < 2**i:
        if local >= 2**n:
            print("No")
            exit()
        if s[count] > p[local]:
            s.append(p[local])
            p[local] = ms
            count += 1
        local += 1
print("Yes")



