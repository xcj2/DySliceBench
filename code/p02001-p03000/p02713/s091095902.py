from sys import stdin
import sys
sys.setrecursionlimit(10000)
import functools
from functools import lru_cache

#from math import gcd

@lru_cache(maxsize=1000000)
def gcd(a,b):
  while b!=0:
    a,b=b,a%b
  return a

def gcdn(nums):
    return functools.reduce(gcd, nums)

@lru_cache(maxsize=1000000)
def gcd3(a,b,c):
   return gcd(gcd(a,b),c)

n = int(stdin.readline().rstrip())

sum = 0
for i in range(n):
    sum += (i+1)
    for j in range(i+1,n):
        sum += 6*gcd(i+1,j+1)
        for k in range(j+1,n):
            #a,b,c = sorted((i+1,j+1,k+1))
            a,b,c = (i+1,j+1,k+1)
            sum += 6*gcdn((a,b,c))

print(sum)
