import bisect
import collections
import copy
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9+7

N,M,P = map(int,(input().split()))
line = []
for i in range(M):
    a,b,c = map(int,(input().split()))
    line.append([a-1,b-1,-c+P])

min_distance = [float("inf")]*N # min_distance[i] は始点から街iまでの最短距離
min_distance[0] = 0 # 始点から始点への最短距離は0とする
#negative = [False]*N

"""
def Bellman_Ford(S,V,E,distance,negative):
    negative = [False]*N
    count = 1
    while count < V:
        count += 1
        for s,g,d in distance: # [s,g,d] = [道路の始点,道路の終点,道路の長さ] について、すべての道路を見る
            if min_distance[s] != float("inf") and min_distance[s] + d < min_distance[g]: # 最短経路が確立されている街から伸びる道路を通ることで、距離を短くできるならば、
                min_distance[g] = min_distance[s] + d # 最短距離を上書きする
                negative[s],negative[g] = True,True
    return min_distance,negative

min_distance,negative = Bellman_Ford(1,N,M,line,negative)
ans = min_distance[N-1]

negative = [False]*N
min_distance,negative = Bellman_Ford(1,N,M,line,negative)
print(negative)
print(min_distance)

if negative[N-1]:
    print(-1)
else:
    print(max(-ans,0))
"""
def Bellman_Ford(S,V,E,distance):
    update = False
    flag = 0
    for _ in range(V):
        for s,g,d in distance: # [s,g,d] = [道路の始点,道路の終点,道路の長さ] について、すべての道路を見る
            if min_distance[s] != float("inf") and min_distance[s] + d < min_distance[g]: # 最短経路が確立されている街から伸びる道路を通ることで、距離を短くできるならば、
                min_distance[g] = min_distance[s] + d # 最短距離を上書きする
                update = True
        if not update:
            flag = 1
            break
    return min_distance,flag

def Bellman_Ford2(S,V,E,distance):
    for _ in range(V):
        for s,g,d in distance: # [s,g,d] = [道路の始点,道路の終点,道路の長さ] について、すべての道路を見る
            if min_distance[s] != float("inf") and min_distance[s] + d < min_distance[g]: # 最短経路が確立されている街から伸びる道路を通ることで、距離を短くできるならば、
                min_distance[g] = -float("inf")
    return min_distance

min_distance,flag = Bellman_Ford(1,N,M,line)

if flag == 1:
    ans = min_distance[N-1]
    print(max(-ans,0))
else:
    min_distance = Bellman_Ford2(1,N,M,line)
    ans = min_distance[N-1]
    if ans == -float("inf"):
        print(-1)
    else:
        print(max(-ans,0))

#print(min_distance)