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
    a = [LI() for _ in range(3)]
    for i in range(3):
        a[i][2] -= a[i][1]
        a[i][1] -= a[i][0]
    if a[0][1] != a[1][1] or a[0][1] != a[2][1] or a[0][2] != a[1][2] or a[0][2] != a[2][2]:
        return 'No'

    return 'Yes'


print(main())


