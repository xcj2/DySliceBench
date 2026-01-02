import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


h, w = li()
grid = [lc() for _ in range(h)]


lr = [[0]*w for _ in range(h)]
tb = [[0]*w for _ in range(h)]

for row in range(h):
    for col in range(w):
        if col == 0:
            lr[row][col] = 1 if grid[row][col] == "." else 0

        else:
            if grid[row][col] == "#":
                continue

            else:
                lr[row][col] = lr[row][col-1] + 1

for row in range(h):
    for col in range(w-2, -1, -1):
        if lr[row][col] == 0:
            continue
        else:
            lr[row][col] = max(lr[row][col+1], lr[row][col])

for col in range(w):
    for row in range(h):
        if row == 0:
            tb[row][col] = 1 if grid[row][col] == "." else 0

        else:
            if grid[row][col] == "#":
                continue
            else:
                tb[row][col] = tb[row-1][col] + 1

for col in range(w):
    for row in range(h-2, -1, -1):
        if tb[row][col] == 0:
            continue
        else:
            tb[row][col] = max(tb[row+1][col], tb[row][col])

ans = 0
for row in range(h):
    for col in range(w):
        ans = max(ans, lr[row][col] + tb[row][col])

print(max(0, ans-1))