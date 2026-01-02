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

n,x = m()
l = l()

co = 0

ans = 1

for i in range(n):
    co += l[i]
    if co <= x:
        ans += 1

print(ans)

