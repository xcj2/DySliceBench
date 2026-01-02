import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)


def main():
    n,a,b,c,d = LI_()
    n += 1
    s = S()
    if d < c:
        f = 0
        for i in range(max(0,b-1), min(min(n-1,d), c-1)):
            if s[i:i+3] == '...':
                f = 1
                break
        if f == 0:
            return 'No'

    for i in range(a+1,c-1):
        if s[i:i+2] == '##':
            return 'No'
    for i in range(b+1,d-1):
        if s[i:i+2] == '##':
            return 'No'


    return 'Yes'


print(main())

