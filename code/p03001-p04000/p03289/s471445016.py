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
    if s[0] != 'A':
        return 'WA'
    c = collections.Counter(s)
    if c['A'] != 1 or c['C'] != 1:
        return 'WA'
    if c['B'] > 0:
        return 'WA'
    for t in string.ascii_uppercase[3:]:
        if c[t] > 0:
            return 'WA'
    if 'C' not in s[2:-1]:
        return 'WA'
    return 'AC'


print(main())
