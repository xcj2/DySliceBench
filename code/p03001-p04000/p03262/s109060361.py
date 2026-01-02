import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

from functools import reduce

# gcdを求める
def findGCD(a:int, b:int) -> int:
    # ユークリッドの互除法
    while 1:
        if a%b == 0:
            return b
        else:
            a = a%b
        
        if b%a == 0:
            return a
        else:
            b = b%a

n,x = li()
a = li()

a_diff = [abs(ai - x) for ai in a]
ans = reduce(findGCD, a_diff)

print(ans)