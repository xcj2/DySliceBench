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
a = list(li())

mx = max(a)
a.remove(mx)

cur = 10**18
ai = 0

for ai in a:
    if abs(ai - mx//2) < cur:
        cur = abs(ai-mx//2)
        ans = ai
        
print(mx, ans)