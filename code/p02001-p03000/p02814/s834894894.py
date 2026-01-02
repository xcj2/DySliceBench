from itertools import permutations
import sys

sys.setrecursionlimit(10 ** 6)
from bisect import *
from collections import *
from heapq import *

def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def SI(): return sys.stdin.readline()[:-1]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
int1 = lambda x: int(x) - 1
def MI1(): return map(int1, sys.stdin.readline().split())
def LI1(): return list(map(int1, sys.stdin.readline().split()))
p2D = lambda x: print(*x, sep="\n")
dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def gcd(a,b):
    while b:a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def main():
    n,k=MI()
    aa=LI()
    aa2=[a//2 for a in aa]
    l=1
    for a2 in aa2:l=lcm(l,a2)
    for a2 in aa2:
        if l//a2%2==0:
            print(0)
            exit()
    print((k//l+1)//2)

main()
