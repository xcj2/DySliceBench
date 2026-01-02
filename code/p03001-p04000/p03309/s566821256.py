import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from heapq import heappop, heappush, heapify, heappushpop
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N = INT()
A = LIST()

# for i in A:
# 	if x-i-1 < 0:
# 		minus.append(x-i-1)
# 	elif x-i-1 == 0:
# 		zero.append(0)
# 	else:
# 		plus.append(-(x-i-1))
# if len(zero) + minus and len(zero) > plus:
# 	print(sum(plus)+sum(minus))
# else:
# 	len(minus) > len(zero) and 
B = [x-i-1 for i, x in enumerate(A)]
B.sort()
# print(B)
B = [abs(x-B[len(B)//2]) for x in B]
# print(B)
print(sum(B))
# print(sum(B)-abs(B[len(B)//2])*N)
