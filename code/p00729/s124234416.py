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
        n,m = LI()
        if n == 0 and m == 0:
            break

        r = I()
        a = [LI() for _ in range(r)]
        q = I()
        b = [LI() for _ in range(q)]
        for s,e,c in b:
            t = 0
            ins = -1
            inc = 0
            for tt,nn,mm,ss in a:
                if mm != c:
                    continue
                if ss == 1:
                    inc += 1
                    if ins < 0:
                        ins = max(tt,s)
                else:
                    inc -= 1
                    if inc == 0:
                        t += max(0, min(e,tt)-ins)
                        ins = -1

            rr.append(t)

    return '\n'.join(map(str, rr))


print(main())


