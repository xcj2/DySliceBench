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
grid = [lc() for _ in range(h)]
new_h = []
new_w = []

for hi in range(h):
    if "#" in grid[hi]:
        new_h.append(hi)

for wj in range(w):
    for hi in range(h):    
        if "#" in grid[hi][wj]:
            new_w.append(wj)
            break
        
ans = [["" for _ in range(len(new_w))] for _ in range(len(new_h))]

for i,nhi in enumerate(new_h):
    for j,nwj in enumerate(new_w):
        ans[i][j] = grid[nhi][nwj]
        
for row in ans:
    print("".join(row))