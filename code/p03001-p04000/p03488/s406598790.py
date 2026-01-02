import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
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

s = input()
x, y = MAP()

x_list = []
y_list = []
for i, s_ in enumerate(s.split('T')):
	if i == 0:
		x -= len(s_)
	elif i % 2 == 0:
		x_list.append(len(s_))
	else:
		y_list.append(len(s_))

def check(d, x):
  se =set([0])
  for dx in d:
    se={a+b for a,b in product(se,[-dx,dx])}  # 直積としてDPを計算
  return (x in se)

print('Yes' if check(x_list, x) and check(y_list, y) else 'No')
