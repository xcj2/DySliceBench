import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353

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

    d = [(0,1),(0,-1),(1,0),(-1,0)]

    while True:
        w,h = LI()
        if w == 0 and h == 0:
            break

        a = [S() for _ in range(h)]
        b = [[0]*w for _ in range(h)]
        c = [[0]*w for _ in range(h)]
        q = []
        for i in range(h):
            for j in range(w):
                if a[i][j] == 'B':
                    q.append((i,j))
        qi = 0
        f = [[None]*w for _ in range(h)]
        while len(q) > qi:
            i,j = q[qi]
            qi += 1
            for di,dj in d:
                ni = di + i
                nj = dj + j
                if 0 <= ni < h and 0 <= nj < w and f[ni][nj] is None:
                    f[ni][nj] = 1
                    if a[ni][nj] == '.':
                        q.append((ni,nj))
                        b[ni][nj] = 1

        q = []
        for i in range(h):
            for j in range(w):
                if a[i][j] == 'W':
                    q.append((i,j))
        qi = 0
        f = [[None]*w for _ in range(h)]
        while len(q) > qi:
            i,j = q[qi]
            qi += 1
            for di,dj in d:
                ni = di + i
                nj = dj + j
                if 0 <= ni < h and 0 <= nj < w and f[ni][nj] is None:
                    f[ni][nj] = 1
                    if a[ni][nj] == '.':
                        q.append((ni,nj))
                        c[ni][nj] = 1
        bc = wc = 0
        for i in range(h):
            for j in range(w):
                if b[i][j] == 1 and c[i][j] == 0:
                    bc += 1
                elif c[i][j] == 1 and b[i][j] == 0:
                    wc += 1


        rr.append('{} {}'.format(bc,wc))

    return '\n'.join(map(str, rr))


print(main())


