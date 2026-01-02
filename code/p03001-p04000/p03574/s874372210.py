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


def main():
    h,w = LI()
    a = [[0]*w for _ in range(h)]
    s = [S() for _ in range(h)]
    for i in range(h):
        si = s[i]
        for j in range(w):
            if si[j] != '#':
                continue
            if j < w-1:
                a[i][j+1] += 1
                if i < h-1:
                    a[i+1][j+1] += 1
                if i > 0:
                    a[i-1][j+1] += 1
            if j > 0:
                a[i][j-1] += 1
                if i < h-1:
                    a[i+1][j-1] += 1
                if i > 0:
                    a[i-1][j-1] += 1

            if i < h-1:
                a[i+1][j] += 1
            if i > 0:
                a[i-1][j] += 1

    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                a[i][j] = '#'

    return '\n'.join([''.join(map(str, r)) for r in a])


print(main())


