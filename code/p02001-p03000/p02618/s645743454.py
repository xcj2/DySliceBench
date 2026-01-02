import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
# input = sys.stdin.readline 
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_list(N): return [s_list() for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    d = i_input()
    c_list = i_list()
    s_list = i_row_list(d)

    last_list = [0] * 26

    for day in range(1,d+1):
        result = 0
        max_point = -INF
        for i in range(26):
            plus_point = s_list[day-1][i]
            minus_point = 0
            for j in range(26):
                if i == j:
                    continue
                minus_point += c_list[j] * (day - last_list[j])
            sum_point = plus_point - minus_point
            if sum_point > max_point:
                result = i + 1
                max_point = sum_point
        print(result)

if __name__ == '__main__':
    main()
