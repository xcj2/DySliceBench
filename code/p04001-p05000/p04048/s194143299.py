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

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

def rec(a: int, b: int) -> int:
    mx = max(a,b)
    mn = min(a,b)
    if gcd(a,b) == mn:
        return (2 * (mx // mn) - 1) * mn
    
    else:
        return (2 * (mx // mn) * mn)  + rec(mn, mx - mn * (mx // mn))
    
n,x = li()
print(n + rec(x, n-x))
    