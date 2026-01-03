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

n = onem()

a = list(input())[:-1]

pata = ["S","W"]

for fi in pata:
    for se in pata:
        aaa = [fi,se]
        for i in range(1,n-1):
            if aaa[-1] == "S":
                if a[i] == "o":
                    aaa.append(aaa[-2])
                else:
                    if aaa[-2] == "S":
                        aaa.append("W")
                    else:
                        aaa.append("S")
            else:
                if a[i] == "o":
                    if aaa[-2] == "S":
                        aaa.append("W")
                    else:
                        aaa.append("S")
                    
                else:
                    aaa.append(aaa[-2])
        flag = True

        if aaa[-1] == "S":
            if a[-1] == "o":
                if aaa[-2] != aaa[0]:
                    flag = False
            else:
                if aaa[-2] == aaa[0]:
                    flag = False
        else:
            if a[-1] == "x":
                if aaa[-2] != aaa[0]:
                    flag = False
            else:
                if aaa[-2] == aaa[0]:
                    flag = False
        if aaa[0] == "S":
            if a[0] == "o":
                if aaa[-1] != aaa[1]:
                    flag = False
            else:
                if aaa[-1] == aaa[1]:
                    flag = False
        else:
            if a[0] == "x":
                if aaa[-1] != aaa[1]:
                    flag = False
            else:
                if aaa[-1] == aaa[1]:
                    flag = False
        if flag:
            print(jo(aaa))
            exit()
print(-1)
exit()





