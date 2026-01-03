from collections import Counter,defaultdict
import sys,heapq,bisect,math,itertools,string,queue
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def conb(n,r): return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n = inp()
a = inpl()
cnt4 = 0
cnt2 = 0
cnt_ = 0
for i in range(n):
    if a[i]%4 == 0:
        cnt4 += 1
    elif a[i]%2 == 0:
        cnt2 += 1
    else :
        cnt_ += 1
if (cnt4+1 == cnt_ and cnt2 == 0) or cnt4 >= cnt_  or cnt2 == n:
    print('Yes')
else:
    print('No')

