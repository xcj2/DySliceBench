from collections import Counter
from collections import defaultdict
import math
import random
import heapq as hq
from math import sqrt
import sys
from functools import reduce


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def tinput():
    return input().split()


def rinput():
    return map(int, tinput())


def rlinput():
    return list(rinput())


mod = int(1e9)+7


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


# ----------------------------------------------------

if __name__ == "__main__":
    a = input()
    b = input()
    n, m = len(a), len(b)
    lcs = [[0 for i in range(n+1)] for j in range(m+1)]


    for i in range(1,m+1):
        for j in range(1,n+1):
            if b[i-1] == a[j-1]:
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i][j-1],lcs[i-1][j])
    
    s=""
    i=m
    j=n
    # print(lcs)
    while i>0 and j>0:
        if b[i-1] == a[j-1]:
            s+=b[i-1]
            i-=1
            j-=1
        elif lcs[i-1][j] > lcs[i][j-1]:
            i-=1
        else:
            j-=1

    print(s[::-1])
        

