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
    h,w,d = LI()
    a = [LI() for _ in range(h)]
    q = I()
    lr = [LI() for _ in range(q)]
    t = {}
    for i in range(h):
        for j in range(w):
            t[a[i][j]] = (i,j)


    k = [0] * (h*w+1)
    for i in range(d+1,h*w+1):
        k[i] = k[i-d] + abs(t[i][0] - t[i-d][0]) + abs(t[i][1] - t[i-d][1])
    rr = []
    for l,r in lr:
        rr.append(k[r]-k[l])

    return '\n'.join(map(str,rr))


print(main())


