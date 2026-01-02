import sys
input = sys.stdin.readline

#import numpy as np
import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
#from collections import deque, defaultdict, Counter
#from heapq import heappush, heappop
#from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
#from operator import itemgetter as ig

#sys.setrecursionlimit(10 ** 7)
#nf = 10 ** 20
#INF = float("INF")
#mod = 10 ** 9 + 7

'''
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]
ddn9 = ddn + [(0, 0)]
for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:

def wi(): return list(map(int, sys.stdin.readline().split()))
def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]  # WideIntPoint
def ws(): return sys.stdin.readline().split()
def si(): return int(sys.stdin.readline())  # SingleInt
def ss(): return input()
def hi(n): return [si() for _ in range(n)]
def hs(n): return [ss() for _ in range(n)]  # HeightString
def s_list(): return list(input())
def mi(n): return [wi() for _ in range(n)]  # MatrixInt
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]
def num_grid(n): return [[int(i) for i in sys.stdin.readline().split()[0]] for _ in range(n)]  # NumberGrid
def grid(n): return [s_list() for _ in range(n)]
# 深さ優先探索
def dfs(G, v):
    global time, first_order,seen,last_order
    time += 1
    first_order[v-1] = time   #　行きがけ

    seen[v-1] = True # v を訪問済みにする
    # v から行ける各頂点 next_v について
    for next_v in G[v]:
        if seen[next_v-1]:
            continue
        dfs(G, next_v)

    time += 1
    last_order[v - 1] = time  # 帰りがけ
'''

def main():

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    Q = int(input())
    task = []
    m = 10**20
    M = 0
    for i in range(Q):
        task.append(list(map(int, input().split())))
        m = min(task[i][0], m)
        M = max(task[i][1], M)

    A = [0]
    count = 0
    for i in range(m, M+1):
        if i % 2 != 0:
            if is_prime((i+1)/2) == True and is_prime(i) == True:
                count += 1
                A.append(count)
            else:
                A.append(count)
        else:
            A.append(count)


    for i in range(Q):
        ans = A[task[i][1]-m +1] -A[task[i][0]-m]
        print(ans)


if __name__ == '__main__':
    main()
