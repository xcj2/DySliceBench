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
        n = I()
        if n == 0:
            break

        ii = LI()
        m = inf
        r = '-1'
        for s in range(16):
            for a in range(16):
                for c in range(16):
                    t = s
                    f = [0] * 256
                    for i in ii:
                        t = (a * t + c) % 256
                        f[(t + i) % 256] += 1
                    h = 0
                    for i in range(256):
                        if f[i] == 0:
                            continue
                        h -= f[i] / n * math.log(f[i] / n)
                    if m > h + eps:
                        m = h
                        r = '{} {} {}'.format(s, a, c)

        rr.append(r)


    return '\n'.join(map(str, rr))


print(main())


