#dpでできないかな？
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod=10**9+7

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a // gcd(a, b) * b
a,b,c,d=MI()
u=lcm(c,d)
#print(u)
#1~x mod y==0
'''def div(x,y):
    return int(x/y) '''
'''ansb=b-div(b,c)-div(b,d)+div(b,u)
ansa=a-1-div(a-1,c)-div(a-1,d)+div(a-1,u)'''
ansb=b-b//c-b//d+b//u
ansa=a-1-(a-1)//c-(a-1)//d+(a-1)//u

print(ansb-ansa)
mod = 10**9 + 7