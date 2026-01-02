from collections import Counter
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solve():
    INF = 10**10

    # Union-Findデータ構造
    class UnionFind:
        def __init__(self, numV):
            self.pars = list(range(numV))
            self.ranks = [0] * numV
        def getRoot(self, x):
            par = self.pars[x]
            if par != x:
                self.pars[x] = par = self.getRoot(par)
            return par
        def merge(self, x, y):
            x, y = self.getRoot(x), self.getRoot(y)
            if x == y: return
            if self.ranks[x] < self.ranks[y]:
                self.pars[x] = y
            else:
                self.pars[y] = x
                if self.ranks[x] == self.ranks[y]:
                    self.ranks[x] += 1
        def isSame(self, x, y):
            return self.getRoot(x) == self.getRoot(y)
        def updatePars(self):
            for v in range(len(self.pars)):
                self.getRoot(v)

    N = int(input())
    #pts = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(N)]
    pts = []
    for i in range(N):
        x, y = map(int, input().split())
        x, y = x-1, y-1
        pts.append((x, y, i))

    UF = UnionFind(N)

    # x昇順
    pts.sort(key=lambda x: x[0])
    stack = [(INF, INF, -1)]
    for x, y, i in pts:
        while stack[-1][1] < y:
            x0, y0, i0 = stack.pop()
            UF.merge(i0, i)
        stack.append((x, y, i))

    # x降順
    #pts.sort(key=lambda x: x[0])
    stack = [(-INF, -INF, -1)]
    for x, y, i in reversed(pts):
        while stack[-1][1] > y:
            x0, y0, i0 = stack.pop()
            UF.merge(i0, i)
        stack.append((x, y, i))

    # y昇順
    pts.sort(key=lambda x: x[1])
    stack = [(INF, INF, -1)]
    for x, y, i in pts:
        while stack[-1][0] < x:
            x0, y0, i0 = stack.pop()
            UF.merge(i0, i)
        stack.append((x, y, i))

    # y降順
    #pts.sort(key=lambda x: x[1])
    stack = [(-INF, -INF, -1)]
    for x, y, i in reversed(pts):
        while stack[-1][0] > x:
            x0, y0, i0 = stack.pop()
            UF.merge(i0, i)
        stack.append((x, y, i))


    UF.updatePars()
    #print('# UF.pars:', UF.pars, file=sys.stderr)

    cnt = Counter(UF.pars)
    #print('# cnt:', cnt, file=sys.stderr)

    anss = [0] * N
    for i in range(N):
        anss[i] = cnt[UF.pars[i]]

    print('\n'.join(map(str, anss)))


solve()
