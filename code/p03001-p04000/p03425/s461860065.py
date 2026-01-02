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
    a = [S() for _ in range(n)]
    c = collections.defaultdict(int)
    for s in a:
        if s[0] in 'MARCH':
            c[s[0]] += 1

    r = 0
    t = 'MARCH'
    for i in range(5):
        for j in range(i+1,5):
            for k in range(j+1,5):
                r += c[t[i]] * c[t[j]] * c[t[k]]

    return r


print(main())


