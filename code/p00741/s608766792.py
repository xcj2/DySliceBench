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

    dd = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

    while True:
        w,h = LI()
        if w == 0:
            break
        a = [LI() for _ in range(h)]
        f = collections.defaultdict(bool)
        r = 0
        for i in range(h):
            for j in range(w):
                if f[(i,j)] or a[i][j] == 0:
                    continue
                r += 1
                q = [(i,j)]
                f[(i,j)] = True
                qi = 0
                while len(q) > qi:
                    ci,cj = q[qi]
                    qi += 1
                    for di,dj in dd:
                        ni = ci + di
                        nj = cj + dj
                        if 0 <= ni < h and 0 <= nj < w and a[ni][nj] == 1 and not f[(ni,nj)]:
                            f[(ni,nj)] = True
                            q.append((ni,nj))
        rr.append(r)

    return '\n'.join(map(str, rr))


print(main())


