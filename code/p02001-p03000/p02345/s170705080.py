import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop

#BIG_NUM = 2000000000
BIG_NUM = 2147483647
HUGE_NUM = 9999999999999999
MOD = 1000000007
EPS = 0.000000001


global N
global table

def MIN(A,B):
    if A <= B:
        return A
    else:
        return B


def init(first_N):
    global N
    while N < first_N:
        N *= 2

def update(loc,value):
    global N
    loc += N-1

    table[loc] = value

    if N == 1:
        return

    parent = (loc-1)//2

    while True:
        table[parent] = MIN(table[2*parent+1],table[2*parent+2])

        if parent == 0:
            break

        parent = (parent-1)//2


def query(search_left,search_right,node_id,node_left,node_right):

    if search_right < node_left or search_left > node_right:
        return BIG_NUM
    if search_left <= node_left and search_right >= node_right:
        return table[node_id]
    else:
        left_min = query(search_left,search_right,2*node_id+1,node_left,(node_left+node_right)//2)
        right_min = query(search_left,search_right,2*node_id+2,(node_left+node_right)//2+1,node_right)
        return MIN(left_min,right_min)



first_N,num_query = map(int,input().split())
N = 1
init(first_N)

table = [None]*(2*N-1)

for i in range(2*N-1):
    table[i] = BIG_NUM


for loop in range(num_query):
    command,left,right = map(int,input().split())

    if command == 0:

        update(left,right)

    else:
        print("%d"%(query(left,right,0,0,N-1)))



