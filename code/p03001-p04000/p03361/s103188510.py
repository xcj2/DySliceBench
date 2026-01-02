import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from math import *

sys.setrecursionlimit(10**6)
INF = 10**20
MOD = 10**9+7

def mint():
    return map(int,input().split())
def lint():
    return map(int,input().split())
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])
def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)

H,W = mint()
S = [input() for _ in range(H)]

def f(i,j):
    ans = False
    for x,y in [(i+1,j), (i-1,j), (i,j-1), (i,j+1)]:
        if 0<=x<H and 0<=y<W and S[x][y]=='#':
            ans = True
            break
    return ans

for i in range(H):
    for j in range(W):
        if S[i][j]=='#':
            if not f(i,j):
                print('No')
                exit()
print('Yes')