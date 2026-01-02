import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
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
        a = [F() for _ in range(n+3)]
        kd = {}
        for i in range(n+3):
            k = [i**c for c in range(n,-1,-1)]
            kd[(i,)] = [a[i], k]

        for _ in range(n):
            nd = {}
            kl = sorted(list(kd.keys()))
            for i in range(len(kl)):
                k1 = kl[i]
                t1 = kd[k1]
                if t1[-1][-1] == 0:
                    nd[k1] = [t1[0], t1[1][:-1]]
                    continue
                for j in range(i+1,len(kl)):
                    k2 = kl[j]
                    sf = 0
                    for c in k1:
                        if c not in k2:
                            sf += 1
                    if sf != 1:
                        continue
                    t2 = kd[k2]
                    if t2[-1][-1] == 0:
                        continue
                    w = t2[-1][-1] / t1[-1][-1]
                    mt = t2[0] - t1[0] * w
                    ma = [c2 - c1*w for c1,c2 in zip(t1[-1][:-1],t2[-1][:-1])]
                    mk = tuple(sorted(set(k1) | set(k2)))
                    nd[mk] = [mt, ma]
            kd = nd
        msa = inf
        msi = -1
        kl = sorted(list(kd.keys()))
        # for k in kl:
            # print(k, kd[k], kd[k][0] / kd[k][1][0] if abs(kd[k][1][0]) > eps else 'none')
        for i in range(n+3):
            mi = inf
            ma = -inf
            for k in kl:
                if i in k or abs(kd[k][1][0]) < eps:
                    # print('not int', i, k)
                    continue
                t = kd[k][0] / kd[k][1][0]
                # print('in', i,t,k)
                if mi > t:
                    mi = t
                if ma < t:
                    ma = t
            sa = ma - mi
            # print(i,ma,mi,sa)
            if msa > sa:
                msa = sa
                msi = i

        return msi


    while 1:
        n = I()
        if n == 0:
            break
        rr.append(f(n))
        # print('rr', rr[-1])

    return '\n'.join(map(str,rr))


print(main())

