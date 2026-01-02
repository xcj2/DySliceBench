# Template 1.0
import sys, re
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from heapq import heappush, heappop, heapify, nlargest, nsmallest
def STR(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def sortListWithIndex(listOfTuples, idx):   return (sorted(listOfTuples, key=lambda x: x[idx]))
def sortDictWithVal(passedDic):
    temp = sorted(passedDic.items(), key=lambda kv: (kv[1], kv[0]))
    toret = {}
    for tup in temp:
        toret[tup[0]] = tup[1]
    return toret
def sortDictWithKey(passedDic):
    return dict(OrderedDict(sorted(passedDic.items())))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def nu_of_factors1(n):
    result_set = set()
    sqrtn = int(n**0.5)
    for i in range(1,sqrtn+1):
        q, r = n/i, n%i
        if r == 0:
            result_set.add(q)
            result_set.add(i)
    return len(result_set)


def getDivisors(n):
    # Note that this loop runs till square root
    factors = []
    i = 1
    while i <= sqrt(n):

        if (n % i == 0):

            # If divisors are equal, print only one
            if (n / i == i):
                factors.append(i)
            else:
                # Otherwise print both
                factors.append(i)
                factors.append(n//i)
        i = i + 1
    return factors

n = INT()
ans = 0

ans+=nu_of_factors1(n-1) - 1

divisors = getDivisors(n)


for el in divisors:
    if(el!=1):
        temp = n
    else:
        continue

    flag = 1
    while(temp!=1):
        if((temp/el).is_integer()):
            temp/=el
            continue
        else:
            if(temp%el==1):
                ans+=1
            flag = 0
            break

    if(flag==1):
        ans+=1
print(ans)