import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353

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

    while True:
        a = [c for c in S()]
        l = len(a)
        s = I()
        t = int(a[0])
        for i in range(len(a)//2):
            if a[i*2+1] == '+':
                t += int(a[i*2+2])
            else:
                t *= int(a[i*2+2])
        u = eval(''.join(a))
        r = 'I'
        if s == u:
            if s == t:
                r = 'U'
            else:
                r = 'M'
        elif s == t:
            r = 'L'

        rr.append(r)
        break


    return '\n'.join(map(str, rr))


print(main())


