import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N = I()
    maxA = -1
    max2A = -1
    max_i = -1
    for i in range(N):
        a = I()
        if a > maxA:
            max2A = maxA
            maxA = a
            max_i = i
        else:
            max2A = max(max2A, a)
    for i in range(N):
        if i != max_i:
            print(maxA)
        else:
            print(max2A)

main()

