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

d = ni()

if d == 25:
    print('Christmas')
    
elif d == 24:
    print('Christmas Eve')
    
elif d == 23:
    print('Christmas Eve Eve')
    
elif d == 22:
    print('Christmas Eve Eve Eve')