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
s = ns()

lb = 0
lw = 0
rb = s.count('#')
rw = s.count('.')

ans = float('inf')

for i, si in enumerate(s):
    if si == '#':
        rb -= 1
    else:
        rw -= 1
        
    ans = min(ans, rw + lb)
    
    if si == '#':
        lb += 1
    else:
        lw += 1
        
print(ans)