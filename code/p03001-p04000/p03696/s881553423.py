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
    s = S()
    d = collections.defaultdict(int)
    for c in s:
        d[c] += 1
    l = d['(']
    r = d[')']

    if l > r:
        s += ')' * (l-r)
    elif r > l:
        s = '(' * (r-l) + s

    c = 0
    rc = 0
    i = 0
    while i < len(s):
        if s[i] == '(':
            c += 1
        else:
            c -= 1
        if c < 0:
            rc += 1
            c = 0
        i += 1
    s = '(' * rc + s + ')' * rc
    return s


print(main())
