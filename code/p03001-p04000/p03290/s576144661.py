import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

import pdb

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
    D, G = LI()
    p, c = [], []
    for _ in range(D):
        _p, _c = LI()
        p.append(_p)
        c.append(_c)

    min_num_solved = inf
    
    for i in range(1 << D):
        point = 0
        num_solved = 0
        unsolved_max = 0
        for j in range(D):
            solve_all = (i >> j) & 1
            if solve_all:
                point += (j+1) * 100 * p[j] + c[j]        
                num_solved += p[j]
            else:
                unsolved_max = max(unsolved_max, j)
         
        if point < G:
            residue = G - point
            p_num = p[unsolved_max]
            while residue > 0 and p_num > 0:
                residue -= (unsolved_max+1) * 100 
                p_num -= 1
                num_solved += 1
            if residue > 0:
                continue
        min_num_solved = min(min_num_solved, num_solved)
    print(min_num_solved)    



main()

