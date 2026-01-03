import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n = I()
    a = [collections.defaultdict(int) for _ in range(n)]
    for i in range(n):
        ai = a[i]
        s = S()
        for c in s:
            ai[c] += 1
    r = ''
    for c in string.ascii_lowercase:
        cc = min([t[c] for t in a])
        r += c * cc
    return r



print(main())
