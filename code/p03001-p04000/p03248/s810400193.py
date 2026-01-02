import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
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
    s = [int(c) for c in S()]
    if s[0] != 1 or s[-1] == 1:
        return -1
    n = len(s)
    for i in range(1,n):
        if s[i-1] != s[n-i-1]:
            return -1

    q = collections.deque()
    for i in range(1,n):
        if s[i] == 1:
            q.append(i+1)
    q.append(n)
    c = 1
    r = []
    for i in range(1,n):
        if c == i:
            c = q.popleft()
        r.append('{} {}'.format(i,c))

    return '\n'.join(r)


print(main())
