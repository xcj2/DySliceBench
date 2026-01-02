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
    rr = []

    def f(n):
        t = int((n * 2) ** 0.5) + 1
        for i in range(t,1,-1):
            if i % 2 == 1:
                if n % i == 0 and  n // i > i // 2:
                    return '{} {}'.format(n//i-i//2, i)
            else:
                if n%i != 0 and n*2 % i == 0 and n // i + 1 > i // 2:
                    return '{} {}'.format(n//i-i//2+1, i)
        return '{} {}'.format(n, 1)

    while 1:
        n = I()
        if n == 0:
            break
        rr.append(f(n))
        # print('nrr',n,rr[-1])

    return '\n'.join(map(str, rr))


print(main())

