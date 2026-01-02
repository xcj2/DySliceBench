import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy
from test.support import _MemoryWatchdog

BIG_NUM = 2000000000
HUGE_NUM = 99999999999999999
MOD = 1000000007
EPS = 0.000000001
sys.setrecursionlimit(100000)


class Edge:
    def __init__(self,arg_to,arg_dist):
        self.to = arg_to
        self.dist = arg_dist

class Info:
    def __init__(self,arg_node_id,arg_sum_dist):
        self.node_id = arg_node_id
        self.sum_dist = arg_sum_dist

    def __lt__(self,another):
        return self.sum_dist < another.sum_dist


V = int(input())
G = [[] for _ in range(V)] #隣接グラフ
min_dist = [BIG_NUM]*V

for _ in range(V):
    node_id,num_adj,*tmp_array = list(map(int,input().split()))
    for i in range(0,len(tmp_array),2):
        G[node_id].append(Edge(tmp_array[i],tmp_array[i+1]))

min_dist[0] = 0
Q = []
heappush(Q, Info(0,0))

while len(Q) > 0:
    info = heappop(Q)
    if info.sum_dist > min_dist[info.node_id]:continue
    for e in G[info.node_id]:
        if min_dist[e.to] > info.sum_dist+e.dist:
            min_dist[e.to] = info.sum_dist+e.dist
            heappush(Q, Info(e.to,min_dist[e.to]))

for i in range(V):
    print("%d %d"%(i,min_dist[i]))

