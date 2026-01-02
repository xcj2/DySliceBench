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

a,b,c,x,y = li()

abonly = a*x + b*y

abandc = 0
if x > y:
    abandc = c*(2*y) + a*(x-y)
else:
    abandc = c*(2*x) + b*(y-x)

conly = c*(2*max(x,y))

print(min(abonly, abandc, conly))