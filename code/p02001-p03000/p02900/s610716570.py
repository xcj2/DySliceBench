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

def factorize(n):
    res = []
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            cnt = 0
            while n%i==0:
                n //= i
                cnt += 1
            res.append((i,cnt))
    if n > 1:
        res.append((n,1))
    return res

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def main():
    """ main """
    A,B = map(int, input().split())
    print(len(factorize(gcd(A,B)))+1)

if __name__ == '__main__':
    main()