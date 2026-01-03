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
mod = 10**9 + 7

a="maerd"
b="remaerd"
c="esare"
d="resare"
s="".join(list(reversed(SI())))
n=len(s)
ind=0
while ind<n:
    #print(ind)
    if s[ind:ind+5]==a or s[ind:ind+5]==c:
        ind+=5
    elif s[ind:ind+6]==d:
        ind+=6
    elif s[ind:ind+7]==b:
        ind+=7
    else:
        print("NO")
        sys.exit()
    #print(ind)
if ind==n:
    print("YES")