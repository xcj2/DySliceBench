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

    while True:
        h,w,n = LI()
        a = [S() for _ in range(h)]

        def f(i,j):
            if a[i][j] == a[i][j+1]:
                return False
            b = [[c for c in s] for s in a]
            b[i][j],b[i][j+1] = b[i][j+1],b[i][j]
            ff = True
            while ff:
                ff = False
                for i in range(h-2,-1,-1):
                    for j in range(w):
                        if b[i][j] == '.':
                            continue
                        for k in range(i,h-1):
                            if b[k+1][j] == '.':
                                b[k+1][j],b[k][j] = b[k][j],b[k+1][j]
                            else:
                                break

                t = [[None]*w for _ in range(h)]
                for i in range(h):
                    for j in range(w):
                        if b[i][j] == '.':
                            continue
                        tf = True
                        for k in range(1,n):
                            if i+k >= h or b[i+k][j] != b[i][j]:
                                tf = False
                                break
                        if tf:
                            for k in range(n):
                                t[i+k][j] = 1
                        tf = True
                        for k in range(1,n):
                            if j+k >= w or b[i][j+k] != b[i][j]:
                                tf = False
                                break
                        if tf:
                            for k in range(n):
                                t[i][j+k] = 1
                for i in range(h):
                    for j in range(w):
                        if t[i][j] is None:
                            continue
                        b[i][j] = '.'
                        ff = True

            for i in range(h):
                for j in range(w):
                    if b[i][j] != '.':
                        return False
            return True

        r = 'NO'
        for i in range(h):
            for j in range(w-1):
                if f(i,j):
                    r = 'YES'
                    break
        rr.append(r)
        break

    return '\n'.join(map(str, rr))


print(main())


