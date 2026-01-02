import sys
sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))
sys.setrecursionlimit(10**6)
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & (-i)
def resolve():
    N = ir()
    c = lr()
    ab = [[] for i in range(N)]
    for i in range(N-1):
        a, b = lr()
        ab[a-1].append(b-1)
        ab[b-1].append(a-1)
    tot = N*(N+1)//2
    il = [0]*N
    ol = [0]*N
    cnt = [0]
    def dfs(u, p):
        cnt[0] += 1
        il[u] = cnt[0]
        for i in ab[u]:
            if i != p:
                dfs(i, u)
        ol[u] = cnt[0]
    dfs(0, -1)
    vs = [[] for i in range(N)]
    for i in range(N):
        vs[c[i]-1].append(i)
    sl = Bit(N)
    for i in range(1, N+1):
        sl.add(i, 1)
    for i in range(N):
        his = []
        ans = tot
        tvs = sorted(vs[i], key=lambda x: il[x])[::-1]
        for v in tvs:
            n = 1
            for j in ab[v]:
                if il[j] > il[v]:
                    tmp = sl.sum(ol[j])-sl.sum(il[j]-1)
                    ans -= tmp*(tmp+1)//2
                    n += tmp
            sl.add(il[v], -n)
            his.append([il[v], n])
        tmp = sl.sum(ol[0])-sl.sum(0)
        ans -= tmp*(tmp+1)//2
        for h in his:
            sl.add(h[0], h[1])
        print(ans)
resolve()