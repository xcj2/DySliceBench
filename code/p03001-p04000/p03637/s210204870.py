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

n = ni()
a = list(li())

mod2 = 0
odd = 0
mod0 = 0

for ai in a:
    if ai%4 == 0:
        mod0 += 1
    elif ai%2 == 0:
        mod2 = 1
    else:
        odd += 1
        
odd += mod2


if mod0 >= (odd-1):
    print("Yes")
else:
    print("No")