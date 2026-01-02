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


    while True:
        w,h = LI()
        if h == 0:
            break
        a = [LI() for _ in range(h)]
        cs = LI()

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
                if u[0][0] == h-1 and u[0][1] == w-1:
                    return d

                for ui in range(4):
                    ud = cs[ui]
                    if a[u[0][0]][u[0][1]] == ui:
                        ud = 0
                    di,dj = dd[(u[1]+ui) % 4]
                    ni = u[0][0] + di
                    nj = u[0][1] + dj
                    if ni < 0 or ni >= h or nj < 0 or nj >= w:
                        continue
                    uv = ((ni,nj), (u[1]+ui) % 4)
                    if v[uv]:
                        continue
                    vd = k + ud
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))
            return d

        d = search(((0,0), 1))
        r = inf
        for i in range(4):
            if r > d[((h-1,w-1),i)]:
                r = d[((h-1,w-1),i)]
        rr.append(r)

    return '\n'.join(map(str, rr))



print(main())

