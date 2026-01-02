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

n,m,x = li()
a = list(li())
small = 0
large = 0
for ai in a:
    if ai < x:
        small += 1
    else:
        large += 1

print(min(small, large))