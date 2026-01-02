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
    i = 0
    j = l-1
    r = 0
    while i<j:
        if s[i] == s[j]:
            i+=1
            j-=1
        elif s[i] == 'x':
            r += 1
            i+=1
        elif s[j] == 'x':
            r += 1
            j -= 1
        else:
            return -1
    return r


print(main())


