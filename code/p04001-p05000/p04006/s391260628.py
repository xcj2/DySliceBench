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

n,x = li()
a = li()

mins = [ai for ai in a]
a2 = a+a

ans = sum(mins)
for k in range(n):
    for i in range(n):
        mins[i] = min(mins[i],a2[i+k])
    
    temp = sum(mins)    
    ans = min(ans, temp + k*x)
    
print(ans)