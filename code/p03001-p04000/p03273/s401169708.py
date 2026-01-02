import sys
import math
import itertools
import bisect
from copy import copy,deepcopy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(map(int,input().split()))
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

H,W = I()
maze = [list(s()) for _ in range(H)]
L1 = []
for i in range(H-1,-1,-1):
    if '#' not in maze[i]:
        maze.pop(i)
H = len(maze)
L2 = []
for i in range(W-1,-1,-1):
    Flag = 1
    for j in range(H):
        if maze[j][i] == '#':
            Flag = 0
            break
    if Flag:
        for j in range(H):
            maze[j].pop(i)
for i in range(H):
    print(''.join(maze[i]))