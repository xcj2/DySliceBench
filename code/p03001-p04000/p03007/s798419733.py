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

a = l()
a.sort()
a = cl.deque(a)
aa = []
co = 0
up = a.pop()
do = a.popleft()

for i in range(len(a)):
    if a[i] >= 0:
        aa.append([do,a[i]])
        do -= a[i]
    else:
        aa.append([up,a[i]])
        up -= a[i]    
aa.append([up,do])
print(up-do)
for i in range(n-1):
    print(jo(aa[i]))

