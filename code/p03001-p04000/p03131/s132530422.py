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

    
k,a,b = li()
k += 1

if k <= a:
    print(k)

elif b <= a+2:
    print(k)

else:
    k -= a
    n = k//2
    print(b + (n-1)*(b-a) + bool(k%2))
