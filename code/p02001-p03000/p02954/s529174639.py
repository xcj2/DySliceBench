'''from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
import numpy as np
from fractions import gcd

sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
'''
S = input()
RLlist = [None]*len(S)
location = []
for i in range(len(S)-1):
    if S[i]=='R' and S[i+1] == 'L':
        RLlist[i] = 'r'
        RLlist[i+1] = 'l'
        location.append(i)

location.sort()
def findhigh(x, ylist):
    for i in range(len(ylist)):
        if x < ylist[i]:
            return ylist[i]


def findlow(x, ylist):
    for i in range(len(ylist)):
        if x < ylist[i]:
            return ylist[i-1]
    return ylist[-1]

ans_list = [1 if RLlist[i] != None else 0 for i in range(len(S))]

for i in range(len(S)):
    if S[i] == 'R' and RLlist[i] != 'r':
        high =findhigh(i,location) 
        diff = abs(high-i)
        if diff%2 == 1:
            ans_list[high+1]+=1
        else:
            ans_list[high]+=1
    if S[i] == 'L' and RLlist[i] != 'l':
        low = findlow(i, location)
        diff = abs(low-i)
        if diff%2 == 1:
            ans_list[low+1]+=1
        else:
            ans_list[low]+=1
        

print(*ans_list)