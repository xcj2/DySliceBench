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
co = 0
for i in range(1,n-1):
    a = l[i-1]
    b = l[i]
    c = l[i+1]
    k = [a,b,c]
    k.sort(reverse = True)
    if k[1] == b and k[0] != k[1]:
        co += 1
print(co)

