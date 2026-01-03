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

def operation(box:list, frm:int, to:int):
    box[frm] -= 1
    box[to] += 1
    
n,m = li()
box = [1 for _ in range(n)]
cand = [False for _ in range(n)]
cand[0] = True
ope = []
for _ in range(m):
    x,y = li_()
    ope.append((x,y))
    
for x,y in ope:
    operation(box,x,y)
    if (not cand[y]) and cand[x]:
        cand[y] = True
    
    if cand[x] and box[x] > 0:
        cand[x] = True
        
    elif cand[x] and box[x] == 0:
        cand[x] = False
        
print(sum(cand))