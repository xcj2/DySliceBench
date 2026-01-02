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

n = ni()

txy = [(0,0,0)]
for _ in range(n):
    txy.append(tuple(li()))
 
exist = True

for i in range(n):
    tp,xp,yp = txy[i]
    tn,xn,yn = txy[i+1]
    
    dt = tn-tp
    dx = xn-xp
    dy = yn-yp
    
    if abs(dx) + abs(dy) > dt:
        exist = False
        break
    
    if (dx+dy)%2 != dt%2:
        exist = False
        break
    
if exist:
    print("Yes")
else:
    print("No")