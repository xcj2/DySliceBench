import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    a = I()
    b = I()
    c = I()
    x = I() // 50
    r = [0] * (x+1)
    r[0] = 1
    u = [0] * (x+1)
    for i in range(c):
        if i+1 > x:
            break
        r[i+1] = 1
    for i in range(1,b+1):
        for j in range(x):
            if i*2+j > x:
                break
            u[i*2+j] += r[j]
    for i in range(x+1):
        r[i] += u[i]
    u = [0] * (x+1)
    for i in range(1,a+1):
        for j in range(x):
            if i*10+j > x:
                break
            u[i*10+j] += r[j]
    for i in range(x+1):
        r[i] += u[i]

    return r[x]



print(main())


