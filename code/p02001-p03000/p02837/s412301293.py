import sys

import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
# from bisect import bisect_left, bisect_right, insort_left, insort_right
# from operator import itemgetter as ig
# sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20; INF = float("INF"); ans = 0; tmp = 0; ansli = []; tmpli = []; candili = []; mod = 10 ** 9 + 7
"""dd = [(-1, 0), (0, 1), (1, 0), (0, -1)];
ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)];
ddn9 = ddn + [(0, 0)]
for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:"""
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
def num_grid(n): return [[int(i) for i in sys.stdin.readline().split()[0]] for _ in range(n)]#NumberGrid
def grid(n): return [s_list() for _ in range(n)]

def main():
    n = si()
    ixy = [[] for _ in range(n)]
    for i in range(n):
        for a in range(int(input())):
            ixy[i].append([int(m) - 1 for m in input().split()])

    # 真：0，不親切：-1
    nums = [i for i in range(n)]

    flag = 0  # 全体の枠組みを抜けるためのflag
    ans = 0
    while ans < n and flag == 0:
        for balls in combinations(nums, ans + 1):
            balls = list(balls)  # 合計人数を調べるために使用，真だと仮定

            # 初期化する場所に注意する！！
            queue = deque()
            hash = defaultdict(lambda: -2)

            for h in balls:
                hash[h] = 0
                queue.append(h)

            sign = queue.popleft()
            brefl = 0  # そのballsでの探索を抜けるためのflag
            while brefl == 0:
                for x, y in ixy[sign]:
                    if y == -1:  # 不親切
                        if x in hash and hash[x] == 0:  # 0-> -1 ×
                            flag = 1
                            brefl = 1
                            break  # 矛盾
                        else:  # -2-> -1 ○
                            hash[x] = -1
                    else:  # 真
                        if x not in hash:  # -2-> 0 ○
                            hash[x] = 0
                            queue.append(x)
                            balls.append(x)
                        elif x in hash and hash[x] == -1:  # -1-> 0 ×
                            flag = 1
                            brefl = 1
                            break  # 矛盾

                if queue == deque():
                    break  # 探索終了
                else:
                    sign = queue.popleft()


            if len(balls) > ans and brefl == 0:
                ans = len(balls)
                flag = 0
                break
    print(ans)


if __name__ == '__main__':
    main()