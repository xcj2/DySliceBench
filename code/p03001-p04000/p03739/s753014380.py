# coding: utf-8
# hello worldと表示する
import sys
import numpy
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
from copy import deepcopy
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

n=I()
seq=LI()
'''if seq[0]>0:
    pm=-1
    sm=seq[0]
    count=0
    for i in range(n-1):
        sm=sm+seq[i+1]
        if pm>0:
            if sm<=0:
                count+=1-sm
                sm=1
            pm=-1
        else:
            if sm>=0:
                count+=1+sm
                sm=-1
            pm=1
    print(count)
elif seq[0]<0:
    pm=1
    sm=seq[0]
    count=0
    for i in range(n-1):
        sm=sm+seq[i+1]
        if pm>0:
            if sm<=0:
                count+=1-sm
                sm=1
            pm=-1
        else:
            if sm>=0:
                count+=1+sm
                sm=-1
            pm=1
    print(count)'''
if seq[0]>0:
    pm=-1
    sm=seq[0]
    count=0
    for i in range(n-1):
        sm=sm+seq[i+1]
        if pm>0:
            if sm<=0:
                count+=1-sm
                sm=1
            pm=-1
        else:
            if sm>=0:
                count+=1+sm
                sm=-1
            pm=1
    count1=count
    pm=1
    sm=-1
    count=1+seq[0]
    for i in range(n-1):
        sm=sm+seq[i+1]
        if pm>0:
            if sm<=0:
                count+=1-sm
                sm=1
            pm=-1
        else:
            if sm>=0:
                count+=1+sm
                sm=-1
            pm=1
    count2=count
    print(min(count1,count2))
elif seq[0]<0:
    pm=1
    sm=seq[0]
    count=0
    for i in range(n-1):
        sm=sm+seq[i+1]
        if pm>0:
            if sm<=0:
                count+=1-sm
                sm=1
            pm=-1
        else:
            if sm>=0:
                count+=1+sm
                sm=-1
            pm=1
    count1=count
    pm=-1
    sm=1
    count=1-seq[0]
    for i in range(n-1):
        sm=sm+seq[i+1]
        if pm>0:
            if sm<=0:
                count+=1-sm
                sm=1
            pm=-1
        else:
            if sm>=0:
                count+=1+sm
                sm=-1
            pm=1
    count2=count
    print(min(count1,count2))
else:
    pm=-1
    sm=1
    count=1
    for i in range(n-1):
        sm=sm+seq[i+1]
        if pm>0:
            if sm<=0:
                count+=1-sm
                sm=1
            pm=-1
        else:
            if sm>=0:
                count+=1+sm
                sm=-1
            pm=1
    count1=count
    pm=1
    sm=-1
    count=1
    for i in range(n-1):
        sm=sm+seq[i+1]
        if pm>0:
            if sm<=0:
                count+=1-sm
                sm=1
            pm=-1
        else:
            if sm>=0:
                count+=1+sm
                sm=-1
            pm=1
    count2=count
    print(min(count1,count2))