import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log2,gcd
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits


def input(): return sys.stdin.readline().strip()


def INT(): return int(input())


def MAP(): return map(int, input().split())


def LIST(): return list(map(int, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def main():
    ans=[]

    while 1:
        n = INT()
        if n==0:
            break
        else:
            a=LIST()
            a.sort()
            mi=max(a)
            for i in range(n-1):
                for j in range(i+1,n):
                    mi=min(mi,a[j]-a[i])

            ans.append(mi)

    for x in ans:
        print(x)

if __name__ == '__main__':
    main()

