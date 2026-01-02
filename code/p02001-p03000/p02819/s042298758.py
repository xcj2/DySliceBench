import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

X = INT()

def is_prime(num):
   """ 素数判定 """
   from math import sqrt
   if num < 2:
       return False
   if num in [2, 3, 5]:
       return True
   if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
       return False
   # 疑似素数(2でも3でも割り切れない数字)で次々に割っていく
   prime = 7
   step = 4
   num_sqrt = sqrt(num)
   while prime <= num_sqrt:
       if num % prime == 0:
           return False
       prime += step
       step = 6 - step
   return True

while 1:
	if is_prime(X):
		print(X)
		break
	else:
		X += 1
