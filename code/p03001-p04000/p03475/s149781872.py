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
    n = I()
    a = [LI() for _ in range(n-1)]
    r = []
    for i in range(n-1):
        s = a[i][0] + a[i][1]
        for j in range(i+1,n-1):
            if s <= a[j][1]:
                s = a[j][1]
            else:
                if s % a[j][2] > 0:
                    s += a[j][2] - s % a[j][2]
            s += a[j][0]
        r.append(s)
    r.append(0)

    return '\n'.join(map(str,r))

print(main())


