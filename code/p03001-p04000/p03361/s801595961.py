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
    h,w = LI()
    a = [[c for c in S()] for _ in range(h)]
    ff = True
    for i in range(h):
        for j in range(w):
            if a[i][j] == '.':
                continue
            f = False
            if (i>0 and a[i-1][j] == '#') or (i<h-1 and a[i+1][j] == '#') or (j>0 and a[i][j-1] == '#') or (j<w-1 and a[i][j+1] == '#'):
                f = True
            if not f:
                ff = False
                break
        if not ff:
            break

    if ff:
        return 'Yes'
    return 'No'



print(main())

