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

x = ni()

if x == 1:
    print(1)
    
else:
    ans = 0
    for b in range(2,40):
        for p in range(2,11):
            if ans < b**p <= x:
                ans = b**p
                
            if b**p > x:
                break
            
    print(ans)