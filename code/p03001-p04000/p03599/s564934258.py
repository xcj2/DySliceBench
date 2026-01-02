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

def can_make(num, a, b):
    while num >= 0:
        if num % a == 0 or num % b == 0:
            return True
        num -= a
    return False

def main():
    A, B, C, D, E, F = LI()
    if A > B:
        A, B = B, A
    if C > D:
        C, D = D, C
    max_perc = -1
    max_sugar = -1
    max_water = -1
    for unit in range(A, 31):
        water = unit * 100
        for sugar in range(min(F - water, unit*E)+1):
            # if water + sugar == 2634 and sugar == 934:
            #     import pdb
            #     pdb.set_trace()
            if water + sugar > F:
                continue
            if 100*sugar/(water+sugar) > E:
                continue
            if can_make(sugar, C, D) and can_make(water, 100*A, 100*B):
                perc = sugar/(sugar + water)
                if perc >= max_perc:
                    max_perc = perc
                    max_sugar = sugar
                    max_water = water
    print(max_water + max_sugar, max_sugar)

main()

