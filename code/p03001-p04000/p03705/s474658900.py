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

n,a,b = li()
if a > b:
    print(0)
elif n == 1 and a != b:
    print(0)
elif n == 1:
    print(1)
else:
    print((a+(n-1)*b) - ((n-1)*a+b) + 1)
    