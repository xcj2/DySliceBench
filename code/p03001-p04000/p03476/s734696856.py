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

class Prime():
    def __init__(self, n):
        self.M = m = int(math.sqrt(n)) + 10
        self.A = a = [True] * m
        a[0] = a[1] = False
        self.T = t = []
        for i in range(2, int(math.sqrt(m)) + 1):
            if not a[i]:
                continue
            t.append(i)
            for j in range(i*i,m,i):
                a[j] = False

    def is_prime(self, n):
        return self.A[n]

    def division(self, n):
        d = collections.defaultdict(int)
        for c in self.T:
            while n % c == 0:
                d[c] += 1
                n //= c
            if n < 2:
                break
        if n > 1:
            d[n] += 1
        return d.items()

    def sowa(self, n):
        r = 1
        for k,v in self.division(n):
            t = 1
            for i in range(1,v+1):
                t += math.pow(k, i)
            r *= t
        return r

def main():
    q = I()
    a = [LI() for _ in range(q)]
    pr = Prime(10**10)
    b = [0]
    for i in range(1,10**5+1):
        if i%2==1 and pr.is_prime(i) and pr.is_prime((i+1)//2):
            b.append(b[-1] + 1)
        else:
            b.append(b[-1])
    r = []
    for c,d in a:
        r.append(b[d]-b[c-1])

    return '\n'.join(map(str,r))

print(main())


