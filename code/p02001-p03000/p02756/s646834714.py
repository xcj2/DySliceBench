# Template 1.0
import sys, re
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from heapq import heappush, heappop, heapify, nlargest, nsmallest
def STR(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def sortListWithIndex(listOfTuples, idx):   return (sorted(listOfTuples, key=lambda x: x[idx]))
def sortDictWithVal(passedDic):
    temp = sorted(passedDic.items(), key=lambda kv: (kv[1], kv[0]))
    toret = {}
    for tup in temp:
        toret[tup[0]] = tup[1]
    return toret
def sortDictWithKey(passedDic):
    return dict(OrderedDict(sorted(passedDic.items())))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

s = input()
q = INT()
rev = 0
begg = []
end = []
for _ in range(q):
     temp = input()
     if(len(temp.split())==1):
         rev+=1

     else:
         t,f,c = temp.split()
         if(f=="1"):
             if(rev%2==0):
                 begg.append(c)
                 # s = c + s
             else:
                 end.append(c)
                 # s = s + c
         else:
             if(rev%2==0):
                 end.append(c)
                 # s = s + c
             else:
                 begg.append(c)
                 # s = c + s
abc = "".join(begg[::-1]) + s + "".join(end)
if(rev%2==0):
    print(abc)
else:
    print(abc[::-1])