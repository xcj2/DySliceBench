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

n,y = li()

yuki_max = y // 10000
ichi_max = y // 5000

ans_y = -1
ans_i = -1
ans_h = -1

for yukichi in range(yuki_max+1):
    for ichiyo in range(ichi_max+1):
        hideyo = (y - 10000*yukichi - 5000*ichiyo) // 1000
        if hideyo < 0:
            continue
        
        if yukichi + ichiyo + hideyo == n:
            ans_y = yukichi
            ans_i = ichiyo
            ans_h = hideyo
            break

print(ans_y, ans_i, ans_h)