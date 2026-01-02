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
    ddd = []
    for i in range(-2,3):
        for j in range(1,4):
            if abs(i)+j > 3:
                break
            ddd.append((i,j))

    while True:
        w,h = LI()
        if w == 0:
            break

        a = [LS() for _ in range(h)]
        b = [[int(c) if '1' <= c <= '9' else 0 for c in t] for t in a]

        def search():
            d = collections.defaultdict(lambda: inf)
            q = []
            for i in range(w):
                if a[-1][i] == 'S':
                    for j in [-1,1]:
                        s = (h-1, i, j)
                        d[s] = 0
                        heapq.heappush(q, (0, s))

            v = collections.defaultdict(bool)
            while len(q):
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True
                if a[u[0]][u[1]] == 'T':
                    return k

                for di, dj in ddd:
                    ni = u[0] + di
                    nj = u[1] + dj * u[2]
                    if ni < 0 or ni >= h or nj < 0 or nj >= w or a[ni][nj] == 'X':
                        continue
                    uv = (ni,nj,-u[2])

                    if v[uv]:
                        continue
                    ud = b[ni][nj]
                    vd = k + ud
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))

            return -1

        rr.append(search())

    return '\n'.join(map(str, rr))



print(main())

