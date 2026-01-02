import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n,q = LI()
    s = S()
    aa = [LS() for _ in range(q)]
    ml = -1
    mr = n
    li = -1
    ri = n
    for t,d in aa[::-1]:
        if s[li+1] == t and d == 'L':
            li += 1
            if ml < li:
                ml = li
                if ml == n-1:
                    return 0
        elif li >= 0 and s[li] == t and d == 'R':
            li -= 1
        if s[ri-1] == t and d == 'R':
            ri -= 1
            if mr > ri:
                mr = ri
                if mr == 0:
                    return 0
        elif ri < n and s[ri] == t and d == 'L':
            ri += 1

    r = n - (li + 1) - (n - ri)

    return r


print(main())


