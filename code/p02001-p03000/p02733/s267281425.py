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


def S(): return input()


def MI(): return map(int, input().split())


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True

WHITE = '1'
BLACK = '0'

# def count(graph):


def main():
    H, W, K = MI()
    graph = [None] * H

    for i in range(H):
        graph[i] = [int(v) for v in list(S())]

    ans = 10**9
    for i in range(2 ** (H-1)):
        groups = [0]
        for j in range((H-1)):
            if ((i >> j) & 1):
                groups.append(j+1)
        groups.append(H)

        divide_count = 0
        counter = defaultdict(int)
        impossible = False
        for w in range(W):
            current_counter = defaultdict(int)
            for g in range(1, len(groups)):
                prev_div = groups[g-1]
                div = groups[g]
                total = 0
                for h in range(prev_div, div):
                    total += graph[h][w]
                current_counter[g] += total

            # 無理な場合
            if not all(v <= K for v in current_counter.values()):
                impossible = True
                break

            for k, v in current_counter.items():
                counter[k] += v
                if counter[k] > K:
                    divide_count += 1
                    counter = current_counter
                    break
            # print(groups, counter, divide_count)

        if not impossible:
            # print(groups, divide_count + len(groups) - 2)
            ans = min(ans, divide_count + len(groups) - 2)

    print(ans)


if __name__ == '__main__':
    main()
