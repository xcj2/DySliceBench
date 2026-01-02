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

n,c = li()
d = [list(li()) for _ in range(c)]
initial = [list(li_()) for _ in range(n)] 

mod_col = [[0]*c for _ in range(3)]

for i,initi in enumerate(initial):
    for j, initij in enumerate(initi):
        mod_col[(i+j) % 3][initij] += 1
        
ans = float('inf')
colors = [-1]*3
for c0 in range(c):
    for c1 in range(c):
        for c2 in range(c):
            if c0 == c1 or c1 == c2 or c2 == c0:
                continue
            
            colors = [c0, c1, c2]
            
            tmp = 0
            for modnum in range(3):
                tmp += sum([d[color][colors[modnum]] * mod_col[modnum][color] for color in range(c)])
                
            ans = min(ans, tmp)


print(ans)