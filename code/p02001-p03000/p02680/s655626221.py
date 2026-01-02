import sys

int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    n, m = MI()
    xx = set([0])
    yy = set([0])
    vl = []
    hl = []
    for _ in range(n):
        a, b, c = MI()
        xx.add(a)
        xx.add(b)
        yy.add(c)
        vl.append((a, b, c))
    for _ in range(m):
        a, b, c = MI()
        xx.add(a)
        yy.add(b)
        yy.add(c)
        hl.append((b, c, a))

    dex = list(sorted(xx))
    dey = list(sorted(yy))
    cox = {x: i for i, x in enumerate(dex)}
    coy = {x: i for i, x in enumerate(dey)}
    h = len(dex)
    w = len(dey)

    vlt=[[1]*w for _ in range(h)]
    for x0, x1, y in vl:
        j = coy[y]
        for i in range(cox[x0], cox[x1]):
            vlt[i][j]=0

    hlt=[[1]*w for _ in range(h)]
    for y0, y1, x in hl:
        i = cox[x]
        for j in range(coy[y0], coy[y1]):
            hlt[i][j]=0
    #p2D(vlt)
    #print()
    #p2D(hlt)

    tt = [[False] * w for _ in range(h)]

    def inf():
        print("INF")
        exit()

    def move(ni, nj):
        if tt[ni][nj]: return
        tt[ni][nj] = True
        stack.append((ni, nj))

    si, sj = cox[0], coy[0]
    if si==h-1 or sj==w-1:inf()
    stack = [(si, sj)]
    tt[si][sj] = True
    while stack:
        i, j = stack.pop()

        ni, nj = i, j - 1
        if vlt[i][j]:
            if nj == -1: inf()
            move(ni, nj)

        ni, nj = i, j + 1
        if vlt[ni][nj]:
            if nj == w - 1: inf()
            move(ni, nj)

        ni, nj = i - 1, j
        if hlt[i][j]:
            if ni == -1: inf()
            move(ni, nj)

        ni, nj = i + 1, j
        if hlt[ni][nj]:
            if ni == h - 1: inf()
            move(ni, nj)
    #p2D(tt)

    ans = 0
    for i in range(h - 1):
        for j in range(w - 1):
            if tt[i][j]: ans += (dex[i + 1] - dex[i]) * (dey[j + 1] - dey[j])
    print(ans)

main()
