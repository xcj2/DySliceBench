import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,sqrt
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7
#s=input().rstrip()

N = int(input())
def dfs(s): # 文字列 s で始まる七五三数の個数
    if int(s) > N:
        return 0
    ret = 1 if all(s.count(c) > 0 for c in '753') else 0 
    # s 自体が七五三数なら +1 
    for c in '753':
        ret += dfs(s + c)
    return ret
print(dfs('0')) # 本当は dfs('') と書きたいが 4 行目でのエラーを防ぐため仕方なく

#文字列をどんどん分岐しながら延ばすときにもdfsは使える
#準七五三数を全列挙し、それぞれについて判定