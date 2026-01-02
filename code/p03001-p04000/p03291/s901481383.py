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
    s = S()
    l = len(s)
    r = [[0]*4 for _ in range(l+1)]
    r[0][0] = 1
    for i in range(l):
        c = s[i]
        if c == 'A' or c == '?':
            r[i+1][0] += r[i][0]
            r[i+1][1] += r[i][1] + r[i][0]
            r[i+1][2] += r[i][2]
            r[i+1][3] += r[i][3]
        if c == 'B' or c == '?':
            r[i+1][0] += r[i][0]
            r[i+1][1] += r[i][1]
            r[i+1][2] += r[i][2] + r[i][1]
            r[i+1][3] += r[i][3]
        if c == 'C' or c == '?':
            r[i+1][0] += r[i][0]
            r[i+1][1] += r[i][1]
            r[i+1][2] += r[i][2]
            r[i+1][3] += r[i][3] + r[i][2]
        for j in range(4):
            r[i+1][j] %= mod


    return r[-1][3]


print(main())
