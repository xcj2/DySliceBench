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
ab = []

for _ in range(n):
    ab.append(tuple(li()))
    
ans = 0
while ab:
    a,b = ab.pop()
    a += ans
    
    ans += b - (a%b) if a%b else 0
    
print(ans)