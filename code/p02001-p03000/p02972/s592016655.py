import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
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
n=int(input())
a=[0]
a.extend(lmp())
l=[0]*(n+1)#iの倍数の箱にいくつ玉が入っているか
ans=[]

for i in range(n,0,-1):
    if (l[i]-a[i])%2==1:
        ans.append(i)
        for k in make_divisors(i):
            l[k]+=1

print(len(ans))
print(*ans[::-1])
    