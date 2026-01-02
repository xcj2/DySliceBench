import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
N = int(input())
S = list(input())
Q = int(input())
q_list = [list(input().split()) for _ in range(Q)]

bit_tree = [[0] * (N+1) for _ in range(26)]
def BIT_add(i, tree):
    while i <= N:
        tree[i] += 1
        i += i&(-i)

def BIT_sub(i, tree):
    while i <= N:
        tree[i] -= 1
        i += i&(-i)

def BIT_sum(i, tree):
    s = 0
    while i:
        s += tree[i]
        i -= i&(-i)
    return s

for i in range(N):
    x = ord(S[i]) - ord('a')
    BIT_add(i + 1, bit_tree[x])

for q in range(Q):
    line = q_list[q]
    if line[0] == '1':
        i, c = line[1:]
        i = int(i) - 1
        old_c = ord(S[i]) - ord('a')
        new_c = ord(c) - ord('a')
        BIT_sub(i + 1, bit_tree[old_c])
        BIT_add(i + 1, bit_tree[new_c])
        S[i] = c
    else:
        l, r = map(int, line[1:])
        now = 0
        for i in range(26):
            cnt = BIT_sum(r, bit_tree[i]) - BIT_sum(l - 1, bit_tree[i])
            if cnt > 0:
                now += 1
        print(now)