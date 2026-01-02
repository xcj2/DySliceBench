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
    a = [int(c) for c in S()]
    for i in range(8):
        c = a[0]
        r = [a[0]]
        for j in range(3):
            if i&(2**j):
                c += a[j+1]
                r.append('+')
            else:
                c -= a[j+1]
                r.append('-')
            r.append(a[j+1])
        if c == 7:
            return ''.join(map(str,r)) + '=7'

    return -1



print(main())


