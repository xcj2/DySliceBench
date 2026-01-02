from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors
n = inp()
a = inpl()
now = a[0]
for i in range(1,n):
    now = math.gcd(now,a[i])
if now != 1:
    print('not coprime')
    quit()
se = set()
for x in a:
    for y in make_divisors(x):
        if y == 1: continue
        if y in se:
            print('setwise coprime')
            quit()
        se.add(y)
print('pairwise coprime')