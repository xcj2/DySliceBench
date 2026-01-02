import sys
import math
import itertools
from heapq import heapify, heappop, heappush
from sys import stdin, stdout, setrecursionlimit
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque


# d = defaultdict(lambda: 0)
# setrecursionlimit(10**7)
# inf = float("inf")


##### stdin ####
def LM(t, r): return list(map(t, r))
def R(): return stdin.readline()
def RS(): return R().split()
def I(): return int(R())
def F(): return float(R())
def LI(): return LM(int,RS())
def LF(): return LM(float,RS())
def ONE_SL(): return list(input())
def ONE_IL(): return LM(int, ONE_SL())
def ALL_IL(): return LM(int,stdin)


##### tools #####
def ap(f): return f.append
def pll(li): print('\n'.join(LM(str,li)))
def pljoin(li, s): print(s.join(li))


##### Library ####


##### main #####
def main():
    A,B = LI()
    
    ans = ""
    if A>8 or B>8:
        ans = ":("
    else:
        ans = "Yay!"

    print(ans)

if __name__ == '__main__':
    main()

