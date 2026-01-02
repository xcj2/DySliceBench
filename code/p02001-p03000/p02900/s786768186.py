import sys
from bisect import *
from collections import *
from copy import deepcopy
from heapq import *
from itertools import *
from math import *
from operator import *
from pprint import *

sys.setrecursionlimit(10**8)

input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    ass.sort()
    return ass

def main():
    """ main """
    A,B = map(int, input().split())
    ds = divisor(gcd(A,B))
    if len(ds) == 1:
        print(1)
        return 0
    ds = ds[1:]
    dp = [1]*len(ds)
    for i in range(len(ds)):
        if dp[i]:
            for j in range(i+1,len(ds)):
                if ds[j]%ds[i] == 0:
                    dp[j] = 0
    ans = 1
    for d in dp:
        if d == 1: ans += 1
    print(ans)

if __name__ == '__main__':
    main()