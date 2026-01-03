import sys
from functools import reduce

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

def get_gcd(a:int, b:int) -> int:
    while b:
        a, b = b, a % b
    return a
    
def get_lcm(a:int, b:int) -> int:
    return (a // get_gcd(a,b)) * b


n = ni()
t = [ni() for _ in range(n)]

lcm = reduce(get_lcm, t)

print(lcm)