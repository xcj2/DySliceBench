import sys,collections as cl,bisect as bs,math
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

q = onem()
AAAA = [sorted(l()) for i in range(q)]

for a,b in AAAA:
    x = math.sqrt(a*b)
    y = int(x)
    if x == y:
        if a == b:
            print(y*2 -2)
        else:
            print(y*2 -3)
    else:
        if y*(y+1)< a*b:
            print(y*2-1)
        else:
            print(y*2-2)