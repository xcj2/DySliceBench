import sys
sys.setrecursionlimit(1000000000)
import math
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
def lcm(a, b): return a * b // gcd(a, b)
from itertools import count, permutations
from functools import lru_cache
from collections import deque, defaultdict
from pprint import pprint
ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
INF = float('inf')
N1097 = 10**9 + 7

def meg(f, ok, ng):
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if f(mid):
            ok=mid
        else:
            ng=mid
    return ok
#

def main():
    N = ii()
    A = lmis()
    l = 1
    for a in A:
        l = lcm(l, a)
    print(sum(l//a for a in A) % N1097)


main()
