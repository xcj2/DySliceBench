import sys
from collections import Counter
from collections import deque
import heapq
import math
import fractions
import bisect
import itertools
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))



def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N=int(input())
if N==1:
    print(0)
    exit()
l=make_divisors(N)
ans=0
for i in range(1,len(l)):
    a,b=divmod(N,l[i]-1)
    if a==b:
        ans+=l[i]-1
print(ans)