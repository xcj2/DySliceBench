import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7

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

    t = [10,50,100,500]

    while True:
        n = I()
        if n == 0:
            break
        a = LI()
        sm = [0] * 4
        sm[0] = t[0] * a[0]
        for i in range(1,4):
            sm[i] = sm[i-1] + t[i] * a[i]

        tr = []
        for i in range(3,-1,-1):
            if i == 0 and n > 0:
                tr.append('{} {}'.format(t[i], n//t[i]))
                break
            tn = n - sm[i-1]
            c = (tn + t[i] - 1) // t[i]
            n -= t[i] * c
            if c > 0:
                tr.append('{} {}'.format(t[i], c))
        if len(rr) > 0:
            rr.append('')
        rr += tr[::-1]



    return '\n'.join(map(str, rr))


print(main())


