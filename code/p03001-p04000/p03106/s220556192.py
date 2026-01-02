import sys
from bisect import *
from collections import *
from copy import deepcopy
from datetime import *
from heapq import *
from itertools import *
# from math import *
from operator import *
from pprint import *

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def divider(a):
    res = set()
    for i in range(1,int(a**0.5)+1):
        if a%i == 0:
            res.add(i)
            res.add(a//i)
    res = list(res)
    res.sort()
    return res


def main():
    """ main """
    A,B,K = map(int, input().split())
    arr = divider(gcd(A,B))
    print(arr[-K])

if __name__ == '__main__':
    main()