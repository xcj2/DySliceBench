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

def digit_sum(num:int, base:int) -> int:

    if num < base:
        return num
    else:
        return digit_sum(int(num/base), base) + (num % base)
    
n,a,b = li()

ans = 0
for i in range(n+1):
    if a <= digit_sum(i,10) <= b:
        ans += i
        
print(ans)