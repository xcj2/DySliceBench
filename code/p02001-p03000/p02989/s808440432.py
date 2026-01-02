import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
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
        if aa == x[i+1]:
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

n = onem()
l = l()
if n % 2 == 1:
    print(0)
    exit()
co = 0
l.sort()
ll = [0 for i in range(10**5+1)]

for i in range(n):
    ll[l[i]] += 1

for i in range(1,len(ll)):
    ll[i] += ll[i-1]
    if ll[i] == n//2:
        co += 1
print(co)

