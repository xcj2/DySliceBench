import sys
input=sys.stdin.readline
from collections import deque
from heapq import heappush,heappop
import re

def int_raw():
    return int(input())
 
def ss_raw():
    return input().split()
 
def ints_raw():
    return tuple(map(int, ss_raw()))


def main():
    N ,Q = ints_raw()
    origST = []

    for idx  in range(N):
        S,T,X = ints_raw()
        origST.append([S-X,T-X,X])
    Ds = [int(input()) for _ in range(Q)]

    origST.sort()
    stidx = 0
    cur_set = []
    for q in Ds:

        while stidx < len(origST):
            st = origST[stidx]
            if st[0] > q:
                break
            heappush(cur_set,(st[2],st[1]))
            stidx+=1
        while cur_set and cur_set[0][1] <=q:
            heappop(cur_set)
        if len(cur_set)==0:
            print(-1)
        else:
            print(cur_set[0][0])
main()
