import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
gosa = 1.0 / 10**10
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    N,A,B = LI()
    s = S()
    a = b = 0
    r = []
    for c in s:
        if c == 'a' and a+b < A+B:
            r.append('Yes')
            a += 1
        elif c == 'b' and a+b < A+B and b<B:
            r.append('Yes')
            b += 1
        else:
            r.append('No')
    return '\n'.join(r)


print(main())

