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
    N = I()
    mid_N = math.ceil(N / 2) 

    ans = float('inf')
    for a in range(1,mid_N+1):
        b = N-a

        sum_digit_a = sum(map(int,list(str(a))))
        sum_digit_b = sum(map(int,list(str(b))))

        tmp = sum_digit_a + sum_digit_b
        ans = min(ans, tmp)

    print(ans)

   
if __name__ == '__main__':
    main()

