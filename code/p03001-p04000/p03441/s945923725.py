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
    e = collections.defaultdict(list)
    for _ in range(n-1):
        a,b = LI()
        e[a].append(b)
        e[b].append(a)

    t = -1
    for i in range(n):
        if len(e[i]) > 2:
            t = i
            break
    if t < 0:
        return 1

    def f(i, s):
        c = 0
        t = 0
        for d in e[i]:
            if d == s:
                continue
            r = f(d, i)
            if r == 0:
                c += 1
            else:
                t += r

        if c > 1:
            t += c - 1
        return t

    return f(t, -1)



print(main())


