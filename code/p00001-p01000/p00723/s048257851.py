import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
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
    rr = []

    n = I()
    t = 0
    while t < n:
        t += 1
        s = S()
        e = set()
        for i in range(len(s)):
            s1 = s[:i]
            s2 = s[i:]
            sr1 = s1[::-1]
            sr2 = s2[::-1]
            e.add(s1+s2)
            e.add(sr1+s2)
            e.add(s1+sr2)
            e.add(sr1+sr2)
            e.add(s2+s1)
            e.add(sr2+s1)
            e.add(s2+sr1)
            e.add(sr2+sr1)


        rr.append(len(e))

    return '\n'.join(map(str, rr))


print(main())


