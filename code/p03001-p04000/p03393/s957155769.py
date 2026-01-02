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
    if len(s) < 26:
        for c in string.ascii_lowercase:
            if c not in s:
                return s + c
    if s == ''.join([c for c in string.ascii_lowercase][::-1]):
        return -1
    for i in range(25,-1,-1):
        c = s[i]
        if max([_ for _ in s[i:]]) == c:
            continue
        t = [_ for _ in s[i:]]
        t.sort()
        ci = t.index(c)
        return s[:i] + t[ci+1]


print(main())


