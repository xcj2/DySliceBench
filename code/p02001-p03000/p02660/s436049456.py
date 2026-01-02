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


def primeFactors(n):
    facs = defaultdict(int)
    # Print the number of two's that divide n
    while n % 2 == 0:
        facs[2]+=1
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            facs[i]+=1
            n = n / i

            # Condition if n is a prime
    # number greater than 2
    if n > 2:
        facs[n]+=1

    return facs

n = INT()

factors = primeFactors(n)

canBe = []

for el in factors:
    for po in range(1, 60):
        if(factors[el]<=0):
            break
        canBe.append(int(el**po))
        factors[el]-=1


canBe.sort()
i = 0
ans = 0

while (True):
    if (i >= len(canBe) or canBe[i] > n):
        break
    if(n/canBe[i]==n//canBe[i]):
        n /= canBe[i]
        ans += 1
    i += 1
    # print(n)
print(ans)