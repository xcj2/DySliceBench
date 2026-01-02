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
n,k = li()
s = ns()

prev = '0'

zeros = []
ones = []

cur = 0
for si in s:
    if si == prev:
        cur += 1
        
    else:
        if prev == '0':
            zeros.append(cur)
            prev = '1'
        else:
            ones.append(cur)
            prev = '0'
        cur = 1
        
if prev == '0':
    zeros.append(cur)
else:
    ones.append(cur)
    zeros.append(0)

if len(ones) == 0 or len(zeros) == 0:
    ans = n

else:
    ans = 0
    zero_cum = [0] + list(accumulate(zeros))
    one_cum = [0] + list(accumulate(ones))
    
    if len(zeros) <= k:
        ans = n
    
    else:
        for i in range(len(zeros)-k+1):
            tmp = (zero_cum[i+k] - zero_cum[i])\
                    + (one_cum[min(len(ones), i+k)] - one_cum[max(0, i-1)])
            ans = max(ans, tmp)
        
print(ans)