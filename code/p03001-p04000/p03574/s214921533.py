import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

h,w = li()
field = [["." for _ in range(w+2)]]
for _ in range(h):
    field.append(["."] + lc() + ["."])
field.append(["." for _ in range(w+2)])

dxs = [0, 1, 1, 1, 0, -1, -1, -1]
dys = [-1, -1, 0, 1, 1, 1, 0, -1]

for hi in range(1,h+1):
    for wj in range(1,w+1):
        if field[hi][wj] == "#":
            continue
        ans = 0
        for dy,dx in zip(dys,dxs):
            if field[hi+dy][wj+dx] == "#":
                ans += 1
        
        field[hi][wj] = str(ans)
        
for hi in range(1,h+1):
    print("".join(field[hi][1:-1]))