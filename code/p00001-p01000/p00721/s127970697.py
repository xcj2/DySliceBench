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

    def f(w,h):
        a = ['x'*(w+2)] + ['x' + S() + 'x' for _ in range(h)] + ['x'*(w+2)]
        e = collections.defaultdict(list)
        st = None
        dst = []
        for i in range(1,h+1):
            for j in range(1,w+1):
                if a[i][j] == 'x':
                    continue
                if a[i][j] == 'o':
                    st = (i,j)
                elif a[i][j] == '*':
                    dst.append((i,j))
                for di,dj in dd:
                    if a[i+di][j+dj] == 'x':
                        continue
                    e[(i,j)].append(((i+di,j+dj), 1))

        def search(s):
            d = collections.defaultdict(lambda: inf)
            d[s] = 0
            q = []
            heapq.heappush(q, (0, s))
            v = collections.defaultdict(bool)
            while len(q):
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True

                for uv, ud in e[u]:
                    if v[uv]:
                        continue
                    vd = k + ud
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))

            return d

        sd = search(st)
        for ds in dst:
            if sd[ds] == inf:
                return -1

        dsd = [search(ds) for ds in dst]
        l = len(dst)
        r = inf
        for ta in itertools.permutations(range(l)):
            t = sd[dst[ta[0]]]
            for i in range(l-1):
                t += dsd[ta[i]][dst[ta[i+1]]]
            if r > t:
                r = t

        return r

    while 1:
        n,m = LI()
        if n == 0 and m == 0:
            break
        rr.append(f(n,m))
        # print('rr', rr[-1])

    return '\n'.join(map(str,rr))


print(main())

