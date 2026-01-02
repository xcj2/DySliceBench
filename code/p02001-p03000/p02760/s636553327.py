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
    A = []
    for _ in range(3):
        A.extend(LI())
    N = I()
    for _ in range(N):
        b = I()
        for i, a in enumerate(A):
            if a == b:
                A[i] = -1
    nums = set()
    for i, a in enumerate(A):
        if a == -1:
            nums.add(i)
    bingo = False
    if 0 in nums and 1 in nums and 2 in nums:
        bingo = True
    if 3 in nums and 4 in nums and 5 in nums:
        bingo = True
    if 6 in nums and 7 in nums and 8 in nums:
        bingo = True
    if 0 in nums and 3 in nums and 6 in nums:
        bingo = True
    if 1 in nums and 4 in nums and 7 in nums:
        bingo = True
    if 2 in nums and 5 in nums and 8 in nums:
        bingo = True
    if 0 in nums and 4 in nums and 8 in nums:
        bingo = True
    if 2 in nums and 4 in nums and 6 in nums:
        bingo = True
    if bingo:
        print("Yes")
    else:
        print("No")


main()

