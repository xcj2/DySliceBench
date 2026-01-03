import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**8) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

a,b = li()

if a <= 0 and b >= 0:
    print('Zero')
    
elif a > 0:
    print('Positive')
    
elif b > 0:
    if (-a)%2 == 0:
        print('Positive')
    else:
        print('Negative')
        
else:
    if (a-b)%2 == 0:
        print('Negative')
    else:
        print('Positive')
