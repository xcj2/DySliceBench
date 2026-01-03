import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

n = ni()
i = 1
ans = 10*10
while i*i <= n:
    if n%i == 0:
        f = max(len(str(i)), len(str(n//i)))        
        ans = min(ans, f)
        
    i += 1
    
print(ans)