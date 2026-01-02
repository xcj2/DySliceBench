import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
Max = sys.maxsize
def l():
    return list(map(int,input().split()))
def m():
    return map(int,input().split())
def onem():
    return int(input())
def s(x):
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
def jo(x):
    return " ".join(map(str,x))

n = onem()
if n == 1:
    l()
    print(1)
else:
    a = []
    for i in range(n):
        a.append(l())
    aa = []
    for i in range(n-1):
        for j in range(i,n):
            if not (a[i][0] - a[j][0] == 0 and a[i][1] - a[j][1] == 0):
                aa.append([a[i][0] - a[j][0],a[i][1] - a[j][1]])
                aa.append([a[j][0] - a[i][0],a[j][1] - a[i][1]])
    aa.sort()
    c = 1
    cc = 1
    lp = aa[0]
    for i in range(1,len(aa)):
        if lp == aa[i]:
            c += 1
        else:
            if c >= cc:
                cc = c
            lp = aa[i]
            c = 1
    if c >= cc:
        cc = c


    print(n - cc )
