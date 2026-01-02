from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate
import sys
import bisect
import string
import math
import time


def I(): return int(input())


def MI(): return map(int, input().split())


def S(): return input()


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = {False: 'No', True: 'Yes'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
# sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


show_flg = True
show_flg = False


def main():
    N = I()
    v = LI()
    first_counter = {}
    second_counter = {}

    for i in range(N):
        if i % 2 == 0:
            if v[i] not in first_counter:
                first_counter[v[i]] = 0
            first_counter[v[i]] += 1
        else:
            if v[i] not in second_counter:
                second_counter[v[i]] = 0
            second_counter[v[i]] += 1

    first_items = sorted([(v, k) for k, v in first_counter.items()], reverse=True)
    second_items = sorted([(v, k)
                           for k, v in second_counter.items()], reverse=True)

    # print(first_items, second_items)
    first_counter, first_value = first_items.pop(0)
    second_counter, second_value = second_items.pop(0)

    first_total_count = (N + (2 - 1)) // 2
    second_total_count = N // 2

    if first_value != second_value:
        print(first_total_count - first_counter + second_total_count - second_counter)
    else:
        first_all_replace_count = first_total_count + second_total_count - second_counter
        second_all_replace_count = second_total_count + first_total_count - first_counter
        first_all_next_replace_count = 10 ** 9
        second_all_next_replace_count = 10 ** 9

        if len(first_items) > 0:
            next_first_counter, next_first_value = first_items.pop(0)
            first_all_next_replace_count = first_total_count - next_first_counter + \
                second_total_count - second_counter

        if len(second_items) > 0:
            next_second_counter, next_second_value = second_items.pop(0)
            second_all_next_replace_count = second_total_count - \
                next_second_counter + first_total_count - first_counter

        print(min(first_all_replace_count,
                  second_all_replace_count,
                  first_all_next_replace_count,
                  second_all_next_replace_count))


if __name__ == '__main__':
    main()
