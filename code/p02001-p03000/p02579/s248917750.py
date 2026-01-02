import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]
dij4=[(0,1),(1,0),(-1,0),(0,-1)]

def solve():
    aa = [[-1] * w for _ in range(h)]
    stack = [(si, sj, 0)]

    while stack:
        wall = []
        while stack:
            i, j, d = stack.pop()
            crash = False
            for di, dj in dij4:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
                if aa[ni][nj] != -1: continue
                if ss[ni][nj]: crash = True
                else:
                    aa[ni][nj] = d
                    stack.append((ni, nj, d))
            if crash: wall.append((i, j, d))

        for i, j, d in wall:
            for di in range(-2, 3):
                for dj in range(-2, 3):
                    if di == 0 and dj == 0: continue
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
                    if ss[ni][nj]: continue
                    if aa[ni][nj] != -1: continue
                    aa[ni][nj] = d + 1
                    stack.append((ni, nj, d + 1))

    print(aa[gi][gj])

h,w=MI()
si,sj=MI1()
gi,gj=MI1()
ss=[[1 if c=="#" else 0 for c in SI()] for _ in range(h)]
solve()
