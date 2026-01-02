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

n,k = li()
x = list(li())

ans = 10**18

for st in range(n-k+1):
    ed = st+k-1
    cand = max(abs(x[st]), abs(x[ed]))
    if x[st] * x[ed] < 0:
        cand += 2 * min(abs(x[st]), abs(x[ed]))
        
    ans = min(ans,cand)
    
print(ans)