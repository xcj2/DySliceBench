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
    return " ".join(map(str,x))
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


def main():

    ss = list(input())[:-1]

    ss = s(ss)

    n = len(ss)

    x,y = m()

    x += 8000

    y += 8000

    dpx = set([8000])

    dpy = set([8000])

    ro = 0

    for i in range(1,n+1):
        pop = ss[i-1]
        if pop[0] == "T":
            if pop[1] % 2 == 1:
                ro ^= 1
        else:
            if i == 1:
                dpx = set([8000+pop[1]])
            else:
                if ro == 0:
                    ch = set()
                    for num in dpx:
                        if num + pop[1] <= 16000:
                            ch.add(num + pop[1])    
                        if num - pop[1] >= 0:
                            ch.add(num - pop[1])
                        dpx = ch
                else:
                    ch = set()
                    for num in dpy:
                        if num + pop[1] <= 16000:
                            ch.add(num + pop[1])
                        if num - pop[1] >= 0:
                            ch.add(num - pop[1])
                        dpy = ch

    if x in dpx and y in dpy:
        print("Yes")
    else:
        print("No")

            


if __name__ == "__main__":
    main()
