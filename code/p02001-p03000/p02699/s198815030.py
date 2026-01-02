mod = 10**9+7
import sys
from collections import Counter, defaultdict, deque
from itertools import product, permutations, combinations
from itertools import accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush
from math import ceil,floor
from copy import deepcopy
from heapq import heappop,heappush,heapify
import heapq


# l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
# c = collections.Counter(l)

sys.setrecursionlimit(10 ** 6)

int1 = lambda x: int(x) - 1

# リストの要素を改行を挟んで表示する
p2D = lambda x: print(*x, sep="\n")
# 入力を整数に変換して受け取る
def II(): return int(sys.stdin.readline())

def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())

# 入力全てを整数に変換したものの配列を受け取る
# def LI(): return list(map(int, sys.stdin.readline().split()))
# 入力全てを整数に変換して1引いたものの配列を受け取る
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI(): return list(map(lambda x:int(x), sys.stdin.readline().split()))
def HI(): return list(map(lambda x:int(x)*(-1), sys.stdin.readline().split()))


s,w =MI()
if s>w:
	print('safe')
else:
	print('unsafe')











