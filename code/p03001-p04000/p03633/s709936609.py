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
                
# lcmを求める
def findLCM(a:int, b:int) -> int:

    return (a//findGCD(a,b)) * b


n = ni()
ts = [ni() for _ in range(n)]

lcm = reduce(findLCM,ts)

print(lcm)