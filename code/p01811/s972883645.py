import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

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

    m = {}
    m['ABC'] = True
    def f(s):
        if s in m:
            return m[s]
        t = s.replace('ABC', 'x')
        if s == t:
            m[s] = False
            return False
        for c in 'ABC':
            if c in t:
                continue
            if f(t.replace('x',c)):
                return True
        m[s] = False
        return False

    if f(s):
        return 'Yes'

    return 'No'


print(main())


