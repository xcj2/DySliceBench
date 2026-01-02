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
        M,T,P,R = LI()
        if M == 0 and T == 0 and P == 0 and R == 0:
            break
        a = [LI() for _ in range(R)]
        d = collections.defaultdict(int)
        tt = [[0,0,i] for i in range(1,T+1)]
        for m,t,p,j in a:
            if j != 0:
                d[(t,p)] += 1
                continue
            tt[t-1][0] += 1
            tt[t-1][1] += m + d[(t,p)] * 20
        tt.sort(key=lambda x: [-x[0],x[1],-x[2]])
        r = str(tt[0][2])
        c = (tt[0][0],tt[0][1])
        for p,m,t in tt[1:]:
            if c == (p,m):
                r += '='
            else:
                r += ','
            r += str(t)
            c = (p,m)
        rr.append(r)

    return '\n'.join(map(str, rr))


print(main())


