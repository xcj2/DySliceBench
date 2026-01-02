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

from itertools import accumulate
from bisect import bisect_left

n = ni()
a = list(li())
b = list(li())

if sum(a) < sum(b):
    print(-1)
    
else:
    over = []
    lack = 0
    ans = 0
    for ai, bi in zip(a,b):
        if ai < bi:
            ans += 1
            lack += (bi-ai)
        else:
            over.append(ai-bi)
            
    over.sort(reverse=True)
    over = [0] + over
    over = list(accumulate(over))
    cnt = bisect_left(over, lack)
    
    ans += cnt
    print(ans)
            