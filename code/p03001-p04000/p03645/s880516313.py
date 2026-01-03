import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n,m = li()

from1 = set()
toN = set()

for _ in range(m):
    a,b = li()
    if a==1:
        from1.add(b)
    elif b==1:
        from1.add(a)
        
    elif a==n:
        toN.add(b)
    elif b==n:
        toN.add(a)

if from1 & toN:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")