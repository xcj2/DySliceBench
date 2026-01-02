import sys
from collections import Counter, deque, defaultdict
from math import factorial
import heapq, bisect
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

def divs(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)
    divisors.sort()
    return divisors

n = INT()

divs = divs(n)

res = divs[len(divs)//2 -1] + divs[len(divs)//2] -2

print(res)
