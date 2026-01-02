import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def solve():
    xc = [[0] * n for _ in range(1 << n)]
    yc = [[0] * n for _ in range(1 << n)]
    for s in range(1 << n):
        xcs = xc[s]
        ycs = yc[s]
        for i, (x, y, p) in enumerate(xyp):
            xcost = abs(x)
            ycost = abs(y)
            for j, (lx, ly, _) in enumerate(xyp):
                if s >> j & 1 == 0: continue
                if abs(x - lx) < xcost: xcost = abs(x - lx)
                if abs(y - ly) < ycost: ycost = abs(y - ly)
            xcs[i] = xcost * p
            ycs[i] = ycost * p
    # print(xc)

    ans = [inf] * (n + 1)
    for s in range(1 << n):
        k = bin(s).count("1")
        xs = (1 << n) - 1
        while xs > 0:
            xs &= s
            xcs = xc[xs]
            ycs = yc[s - xs]
            cur = 0
            for i in range(n): cur += min(xcs[i], ycs[i])
            if cur < ans[k]: ans[k] = cur
            xs -= 1

    for a in ans: print(a)

inf = 10 ** 16
n = II()
xyp = LLI(n)

solve()
