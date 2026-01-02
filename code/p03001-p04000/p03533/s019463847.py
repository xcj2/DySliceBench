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
    s = S()
    t = 'AKIHABARA'
    l = len(t)
    ti = 0
    for c in s:
        if ti >= l:
            return 'NO'
        if t[ti] == c:
            ti += 1
        else:
            while ti < l and t[ti] == 'A' and t[ti] != c:
                ti += 1
            if ti >= l or t[ti] != c:
                return 'NO'
            ti += 1

    while ti < l and t[ti] == 'A':
        ti += 1
    if ti == l:
        return 'YES'

    return 'NO'



print(main())


