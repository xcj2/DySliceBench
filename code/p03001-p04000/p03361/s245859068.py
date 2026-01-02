import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

h,w = li()

grid = [list(lc()) for _ in range(h)]

dhs = [-1,0,1,0]
dws = [0,-1,0,1]

achive = True

for hi in range(h):
    for wj in range(w):
        ok = False
        if grid[hi][wj] == ".":
            continue
        
        for dh,dw in zip(dhs,dws):
            if 0 <= hi+dh < h and 0 <= wj+dw < w:
                if grid[hi+dh][wj+dw] == "#":
                    ok = True
                    
        if not ok:
            achive = False

print("Yes") if achive else print("No")