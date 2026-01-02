import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
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
    rr = []
    ii = [2**i for i in range(6)]

    while True:
        n = I()
        if n == 0:
            break
        a = [S() for _ in range(n)]
        d = 0
        s = [[]]
        for c in a:
            l = len(c)
            while l <= d:
                if s[-1][0] == '+':
                    k = 0
                    for kc in s[-1][1:]:
                        k += kc
                else:
                    k = 1
                    for kc in s[-1][1:]:
                        k *= kc
                s = s[:-1]
                s[-1].append(k)
                d -= 1

            t = c[-1]
            if t == '+' or t == '*':
                d += 1
                s.append([t])
            else:
                s[-1].append(int(t))

        while len(s) > 1:
            if s[-1][0] == '+':
                k = 0
                for kc in s[-1][1:]:
                    k += kc
            else:
                k = 1
                for kc in s[-1][1:]:
                    k *= kc
            s = s[:-1]
            s[-1].append(k)

        rr.append(s[0][0])


    return '\n'.join(map(str, rr))


print(main())


