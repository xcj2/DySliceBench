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
    l = len(s)
    a = [c == '1' for c in s]
    r = l//2 + l%2
    b = l//2 - 1
    c = l//2 + l%2
    for i in range(b+1):
        if a[b-i] != a[b-i+1] or a[c+i] != a[c+i-1]:
            break
        r += 1

    return r



print(main())


