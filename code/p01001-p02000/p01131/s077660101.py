import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**3
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
    a = [S() for _ in range(n)]
    d = {}
    d[1] = '.,!? '
    d[2] = 'abc'
    d[3] = 'def'
    d[4] = 'ghi'
    d[5] = 'jkl'
    d[6] = 'mno'
    d[7] = 'pqrs'
    d[8] = 'tuv'
    d[9] = 'wxyz'
    for s in a:
        r = ''
        i = -1
        c = 0
        for t in s:
            tc = int(t)
            if tc == 0:
                if c > 0:
                    r += d[c][i%len(d[c])]
                i = -1
                c = 0
            else:
                c = tc
                i += 1
        rr.append(r)

    return '\n'.join(map(str, rr))


print(main())


