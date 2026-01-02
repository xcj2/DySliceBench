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

n,m = m()

l = [l() for i in range(n)]
l.sort(key = lambda x:x[2])
ans = [-1]*m
ju = [-1]*m
d = [onem() for i in range(m)]
for s,t,x in l:
    ore = bs.bisect_left(d,s-x)
    o = bs.bisect_left(d,t-x)
    while (ore < o):
        k = ju[ore]
        if k == -1:
            ans[ore] = x
            ju[ore] = o
            ore += 1
        else:
            ore = k
for i in range(m):
    print(ans[i])
