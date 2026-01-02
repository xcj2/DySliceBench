import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left
from functools import reduce
input = sys.stdin.readline 
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
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    n, k = i_map()
    num_list = i_list()

    trans_list = [0] * n

    next_trans = num_list[0]
    for i in range(n):
        trans_list[i] = next_trans
        next_trans = num_list[next_trans-1]

    # print(trans_list)

    chcek_list = [INF] * n
    for i in range(n):
        if chcek_list[trans_list[i]-1] != INF:
            break
        chcek_list[trans_list[i]-1] = 1

    first_town = trans_list.index(trans_list[i])

    period = i - first_town

    if k <= n:
        print(trans_list[k-1])
    else:
        trans_list = trans_list[first_town:]
        trans_list = trans_list[:period]
        print(trans_list[(k-first_town)%period-1])

if __name__ == '__main__':
    main()
