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
        a = LS()
        r = 'TIE'
        d = collections.defaultdict(int)
        for i in range(n):
            d[a[i]] += 1
            s = sorted(list(d.items()) + [('-', 0)], key=lambda x: [-x[1]])
            if s[0][1] - s[1][1] > n - i - 1:
                r = '{} {}'.format(s[0][0], i+1)
                break

        rr.append(r)

    return '\n'.join(map(str, rr))


print(main())


