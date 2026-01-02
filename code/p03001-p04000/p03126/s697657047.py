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

n,m = li()
vote = [0]*(m+1)
for _ in range(n):
    like = list(li())
    
    for i in like[1:]:
        vote[i] += 1
        
ans = 0
for vi in vote:
    if vi == n:
        ans += 1
        
print(ans)