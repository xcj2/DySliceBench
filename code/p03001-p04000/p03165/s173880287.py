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
    s = [c for c in S()]
    t = [c for c in S()]
    sl = len(s)
    tl = len(t)
    rr = [[0] * (tl) for _ in range(sl)]
    for i in range(sl):
        for j in range(tl):
            if s[i] == t[j]:
                if i > 0 and j > 0:
                    rr[i][j] = rr[i-1][j-1] + 1
                else:
                    rr[i][j] = 1
                continue

            m = 0
            if i > 0:
                m = rr[i-1][j]
            if j > 0 and m < rr[i][j-1]:
                m = rr[i][j-1]
            rr[i][j] = m

    i = sl-1
    j = tl-1
    r = []
    while i >= 0 and j >= 0:
        if s[i] == t[j]:
            r.append(s[i])
            i -= 1
            j -= 1
            continue
        if rr[i][j] == 0:
            break
        if i > 0 and rr[i-1][j] == rr[i][j]:
            i -= 1
        else:
            j -= 1

    return ''.join(r[::-1])


print(main())
