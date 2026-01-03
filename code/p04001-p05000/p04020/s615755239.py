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
a = []
for _ in range(n):
    a.append(ni())
    
res = 0
ans = 0
for ai in a:
    if ai == 0:
        ans += res//2
        res = 0
    else:
        res += ai
        
ans += res//2
    
print(ans)