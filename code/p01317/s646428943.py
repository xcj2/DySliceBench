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

class WarshallFloyd():
    def __init__(self, e, n):
        self.E = e
        self.N = n

    def search(self):
        n = self.N
        nl = list(range(n))
        d = [[inf] * n for _ in nl]
        for i in range(n):
            d[i][i] = 0
        for k,v in self.E.items():
            dk = d[k]
            for b,c in v:
                # consider multiple edges
                if dk[b] > c:
                    dk[b] = c
        for i in nl:
            di = d[i]
            for j in nl:
                if i == j:
                    continue
                dj = d[j]
                for k in nl:
                    if i != k and j != k and dj[k] > dj[i] + di[k]:
                        dj[k] = dj[i] + di[k]
        return d


def main():
    rr = []

    def f(n,m):
        le = collections.defaultdict(list)
        se = collections.defaultdict(list)
        for _ in range(m):
            l = LS()
            a,b,t = map(int, l[:-1])
            a -= 1
            b -= 1
            if l[-1] == 'S':
                se[a].append((b,t))
                se[b].append((a,t))
            else:
                le[a].append((b,t))
                le[b].append((a,t))
        q = I()
        qa = LI_()
        lw = WarshallFloyd(le, n)
        sw = WarshallFloyd(se, n)
        ld = lw.search()
        sd = sw.search()
        dp = [inf] * n
        dp[qa[0]] = 0
        # print('ld')
        # print('\n'.join('\t'.join(map(lambda x: '-' if x == inf else str(x), c)) for c in ld))
        # print('sd')
        # print('\n'.join('\t'.join(map(lambda x: '-' if x == inf else str(x), c)) for c in sd))
        for i in range(q-1):
            c = qa[i]
            ne = qa[i+1]
            lp = [inf] * n
            np = [inf] * n
            for j in range(n):
                np[j] = dp[j] + ld[c][ne]
                dj = dp[j] + ld[c][j]
                sdj = sd[j]
                for k in range(n):
                    if lp[k] > dj + sdj[k]:
                        lp[k] = dj + sdj[k]
            for j in range(n):
                if np[j] > lp[j] + ld[j][ne]:
                    np[j] = lp[j] + ld[j][ne]
            # print('cne', c, ne)
            # print('dp', dp)
            # print('lp', lp)
            dp = np

        # print('edp', dp)
        return min(dp)

    while 1:
        n,m = LI()
        if n == 0 and m == 0:
            break
        rr.append(f(n,m))
        # print('rr', rr[-1])

    return '\n'.join(map(str,rr))


print(main())

