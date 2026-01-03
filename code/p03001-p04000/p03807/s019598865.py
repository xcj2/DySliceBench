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

odd = 0
even = 0

n = ni()
a = list(li())

for ai in a:
    if ai%2:
        odd += 1
    else:
        even += 1
        
if odd%2:
    print("NO")
else:
    print("YES")