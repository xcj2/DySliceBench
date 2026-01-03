import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    w, h, n = MI()
    tt = [[1] * w for _ in range(h)]
    for _ in range(n):
        x, y, a = MI()
        if a == 1: i0, i1, j0, j1 = 0, h, 0, x
        if a == 2: i0, i1, j0, j1 = 0, h, x, w
        if a == 3: i0, i1, j0, j1 = 0, y, 0, w
        if a == 4: i0, i1, j0, j1 = y, h, 0, w
        for i in range(i0, i1):
            for j in range(j0, j1):
                tt[i][j] = 0
    ans=sum(sum(row) for row in tt)
    print(ans)

main()
