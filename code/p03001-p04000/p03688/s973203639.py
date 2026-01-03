import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n = I()
    a = LI()
    d = collections.defaultdict(int)
    for c in a:
        d[c] += 1
    t = sorted(list(d.keys()))
    if t[-1] - t[0] > 1:
        return 'No'
    if len(t) == 1:
        if t[0] == n - 1:
            return 'Yes'
        if t[0] > n / 2.0:
            return 'No'
        return 'Yes'
    b = t[1] - d[t[0]]
    n2 = d[t[1]]
    if n2 == 2 and b == n2 - 1:
        return 'Yes'
    if b < 1:
        return 'No'
    if b >= n2 - 2:
        return 'No'
    if b > n2 / 2.0:
        return 'No'

    return 'Yes'


print(main())
