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
    s = S()
    d = collections.defaultdict(list)
    l = len(s)
    for i in range(l):
        d[s[i]].append(i)

    r = inf
    for c in d.keys():
        t = -1
        rc = 0
        for i in d[c]:
            if rc < i - t - 1:
                rc = i - t - 1
            t = i
        if rc < l - t - 1:
            rc = l - t - 1
        if r > rc:
            r = rc

    return r


print(main())
