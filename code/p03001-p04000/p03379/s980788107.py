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
x = list(li())

med1 = sorted(x)[n//2 - 1]
med2 = sorted(x)[n//2]

for xi in x:
    if xi <= med1:
        print(med2)
    else:
        print(med1)       