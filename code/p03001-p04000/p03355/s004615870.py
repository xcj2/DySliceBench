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

    input_S = input()
    K = I() - 1

    # input_S = 'abcaa'
    # K = 2

    len_S = len(input_S)
    unique_S = len(set(input_S))
    
    lis = set()
    min_s = 'z'

    if len_S == 1:
        print(input_S)

    else:
        for i in range(5):
            for j in range(len_S):
                if input_S[j] > min_s:
                    continue

                s = input_S[j:j+i+1]
                lis.add(s)

        print(sorted(lis)[K])

   
if __name__ == '__main__':
    main()

