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

    for _  in range(N):
        S,T,X = ints_raw()
        origST.append([S-X,T-X,X])
    Ds = [int(input()) for _ in range(Q)]

    origST.sort()
    stidx = 0
    cur_set = []
    for d in Ds:

        while stidx < len(origST):
            st = origST[stidx]
            if st[0] > d:
                break
            heappush(cur_set,(st[2],st[1]))
            stidx+=1
        while cur_set and cur_set[0][1] <=d:
            heappop(cur_set)
        if cur_set:
            print(cur_set[0][0])
        else:
            print(-1)
main()
