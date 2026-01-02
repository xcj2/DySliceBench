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
 
a,b,c = li()
 
a,b,c = sorted([a,b,c])
 
cnt = 0
while a != b or b != c:
    if a != b:
        a += 2
        
    else:
        a += 1
        b += 1
        
    a,b,c = sorted([a,b,c])
        
    cnt += 1
    
    
print(cnt)