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
def pf(s): return print(s, flush=True)

class BIT():
    def __init__(self, n):
        i = 1
        while 2**i <= n:
            i += 1
        self.H = i
        self.N = 2**i
        self.A = [0] * self.N

    def find(self, i):
        r = 0
        while i:
            r += self.A[i]
            i -= i & (i-1) ^ i
        return r

    def update(self, i, x):
        while i < self.N:
            self.A[i] += x
            i += i & (i-1) ^ i

    def query(self, a, b):
        return self.find(b-1) - self.find(a-1)

def main():
    n,q = LI()
    a = [LI() for _ in range(q)]
    b = BIT(n+3)
    r = []
    for c,x,y in a:
        if c == 0:
            b.update(x,y)
        else:
            r.append(b.query(x,y+1))

    return '\n'.join(map(str,r))


print(main())