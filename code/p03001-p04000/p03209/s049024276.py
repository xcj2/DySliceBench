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

a = [1]
p = [1]
for _ in range(51):
    a.append(3 + 2*a[-1])
    p.append(1 + 2*p[-1])

def burger(level: int, x: int):
    if level == 0:
        if x <= 0:
            return 0
        else:
            return 1
    
    if x == 1:
        return 0
    
    elif 1 < x <= 1+a[level-1]:
        return burger(level-1, x-1)
    
    elif x == 2+a[level-1]:
        return p[level-1] + 1
    
    elif 2+a[level-1] < x <= 2+2*a[level-1]:
        return p[level-1] + 1 + burger(level-1, x-1-a[level-1]-1)
    
    elif x == 3+2*a[level-1]:
        return 2*p[level-1] + 1
    
n,x = li()    
print(burger(n,x))
    